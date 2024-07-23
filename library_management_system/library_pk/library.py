from .book import Book
from .structure import Structure
from .person import Person
from.transaction import Transaction
from datetime import datetime
from .display import display_books ,display_transaction
import os
import random
class Library:
    def __init__(self):
        self.struct = Structure()
        self.__active_path = "../library_management_system/assets/active-books/books.bin"
        self.__del_path =  "../library_management_system/assets/deleted-books/archive.bin"
        self.__person_path =  "../library_management_system/assets/persons/person.bin"
        self.__transaction_path =  "../library_management_system/assets/transactions/transaction.bin"
    def add_new_book(self,title,content,author):
        book = Book(title,content,author,datetime.now(),datetime.now())
        book.isAvailable = True
        self.add_book_to_file(book) 
    def del_book(self,book_id):
        found = self.__search_book_from_file(book_id,self.__active_path)
        if found:
            if found.isAvailable:
                check = self.confirm_check()
                if check == 'y':
                    self.update_book(book_id,found.title,found.content,found.author,found.createdAt,datetime.now())
                    self.__del_book_from_file(self.__active_path,book_id)
                    with open(self.__del_path,'ab') as df:
                        found.isAvailable= False
                        found.updatedAt = datetime.now()
                        df.write(self.struct.serialize_data(found))  
                        print("######Book Deleted Succesfully######")
                elif check == 'n':
                    print("######Returned to Main Menu######")
                else:
                    print("!!!!!Invalid Entry!!!!!!")
            else:
                print(f"####Book cannot be deleted as it is assigned to {found.borrowed_name}####")
        else:
            print("#####Book Not found######")
    def permanent_del_book(self,book_id):
        found = self.__search_book_from_file(book_id,self.__del_path)
        if found:
            check = self.confirm_check()
            if check == 'y':
                self.__del_book_from_file(self.__del_path,book_id)
                print("######Book Deleted Permanently Succesfully######")
            elif check == 'n':
                print("######Returned to Main Menu######")
            else:
                print("!!!!!Invalid Entry!!!!!!")
        else:
            print("#### BOOK NOT FOUND ####")
    def view_book(self,params):
        book_data = []
        count=0
        id=1
        if params:
            path = self.__active_path
        else:
            path = self.__del_path
        if os.path.exists(f"{path}"):
            with open(f"{path}","rb") as f:
                while True:
                    data = f.read(self.struct.cal_size())
                    if not data:
                        if count ==0:
                            print("############No Book Available############")
                        break
                    book = self.struct.deserialize_data(data)
                    book_data.append(book)
                    count+=1
                    id+=1
                if len(book_data)>0:
                    display_books(book_data)
        else:
           print("!-!-!-!File Not Found!-!-!-!")
    def __update_book_to_file(self,book_id, updated_book, path):
        with open(f"{self.__active_path}","r+b") as f:
           f.seek(book_id * self.struct.cal_size())
           f.write(self.struct.serialize_data(updated_book))
           return True
    def update_book(self,book_id,title,content,author,createdAt,updatedAt):
        updated_book = Book(title,content,author,createdAt,updatedAt)
        return self.__update_book_to_file(book_id,updated_book, self.__active_path)
    def add_book_to_file(self,book:Book):
        with open(f"{self.__active_path}","ab") as f:
            f.write(self.struct.serialize_data(book))  
    def __del_book_from_file(self,path,book_id):
        with open(path,'rb') as f:
            data = f.read()
        start_pos = book_id * self.struct.cal_size()
        end_pos = start_pos + self.struct.cal_size()
        new_data = data[:start_pos] + data[end_pos:]
        with open(path,'wb') as f:
            f.write(new_data) 
    def __search_book_from_file(self,book_id,path):
        with open(f"{path}","r+b") as f:
            f.seek(book_id * self.struct.cal_size())
            data = f.read(self.struct.cal_size())
            if data:    
                book = self.struct.deserialize_data(data)
                return book
            else:
                return False
    def search_book(self,book_id):
        return self.__search_book_from_file(book_id,self.__active_path)
    def restore_book(self,book_id):
        found = self.__search_book_from_file(book_id,self.__del_path)
        if found:
            check = self.confirm_check()
            if check == 'y':
                self.__del_book_from_file(self.__del_path,book_id)
                found.isAvailable=True
                self.add_book_to_file(found)
                print("######Book Restored Succesfully######")
            elif check == 'n':
                print("######Returned to Main Menu######")
            else:
                print("!!!!!Invalid Entry!!!!!!")
        else:
            print("#### BOOK NOT FOUND ####")
    def confirm_check(self):
        return input("Are you sure. The Action cannot be revert if say yes (Y/N) : ")
    def check_available(self,book_id):
        found = self.search_book(book_id)
        if found.isAvailable:
            return True
        else:
            return False
    def assign_book(self, p1, book,book_id ):
        book.isAvailable = False
        book.borrowed_name = p1.name
        book.borrower_email = p1.pid
        with open(self.__active_path,'r+b') as f:        
            f.seek(book_id * self.struct.cal_size())
            f.write(self.struct.serialize_data(book))
        self.add_transaction(p1,book,book_id,1)
    def add_transaction(self, p1 , book ,book_id, t_type):
        with open(self.__transaction_path,'ab') as tf:
            transaction = Transaction(book_id,book.title , p1.pid, p1.name,t_type )
            tf.write(Transaction.serialize(transaction))
    def return_book(self,p1,book , book_id):
        book.isAvailable = True
        book.borrowed_name = ""
        book.borrower_email = ""
        with open(self.__active_path,'r+b') as f:        
            f.seek(book_id * self.struct.cal_size())
            f.write(self.struct.serialize_data(book))
        self.add_transaction(p1,book,book_id,0)
    def view_Transaction(self):
        id = 1
        trans = []
        with open(self.__transaction_path,'rb') as tf:
            print("")
            while True:
                data = tf.read(Transaction.cal_size())
                if not data:
                    break
                trans_data = Transaction.deserialize(data)
                trans.append(trans_data)
            if len(trans)>0:
                display_transaction(trans)
            else:
                print("##########No Transactions Available##########")