from .book import Book
import pandas as pd
import shutil
import pickle
import os
import random
class Library:
    bookid=10001
    def __init__(self):
        self.__active_path = "../library_management_system/assets/active-books/"
        self.__del_path =  "../library_management_system/assets/deleted-books/"
        with open("../library_management_system/assets/current_id.txt","r") as f:
            Library.bookid = int(f.read())
    def add_book_to_file(self,book:Book):
        with open(f"{self.__active_path}{Library.bookid}","wb") as f:
            pickle.dump(book,f)     
    def add_new_book(self,title,content,author):
        book = Book(title,content,author,False)
        self.add_book_to_file(book)
        Library.bookid+=1
        with open("../library_management_system/assets/current_id.txt","w") as fw:
            fw.write(str(Library.bookid))
    def del_book(self,book_id):
        if os.path.exists(f"{self.__active_path}{book_id}"):
            check = self.confirm_check()
            if check == 'y':
                data = self.search_book(book_id)
                self.update_book(book_id,data.title,data.content,data.author,data.createdAt)
                shutil.move(f"{self.__active_path}{book_id}",f"{self.__del_path}{book_id}")
            elif check == 'n':
                print("no action perform")
            else:
                print("Invalid Entry")
        else:
            print("The Book does not exist")
    def permanent_del_book(self,book_id):
        if os.path.exists(f"{self.__del_path}{book_id}"):
            check = self.confirm_check()
            if check == 'y':
                os.remove(f"{self.__del_path}{book_id}")
            elif check == 'n':
                print("no action perform")
            else:
                print("Invalid Entry")
        else:
            print("The Book does not exist")
    def view_book(self,params):
        print(f"ID      title       content     author      createdAt    updatedAt")
        if params:
            path = self.__active_path
        else:
            path = self.__del_path
        dir_list = os.listdir(path)
        for file in dir_list:
            if os.path.exists(f"{path}{file}"):
                with open(f"{path}{file}","rb") as f:
                    mb = pickle.load(f)
                    print(f"{file}       {mb.title}      {mb.content}     {mb.author}     {mb.createdAt}      {mb.updatedAt}")
            else:
                print("No Book Available ")
        else:
            print("No Book Available")
    def update_book(self,book_id,title,content,author,createdAt):
        book = Book(title,content,author,createdAt)
        with open(f"{self.__active_path}{book_id}","wb") as f:
            pickle.dump(book,f)
    def search_book(self,book_id):
        if os.path.exists(f"{self.__active_path}{book_id}"):
            print(f"ID      title       content     author      createdAt    updatedAt")
            with open(f"{self.__active_path}{book_id}","rb") as f:
                mb = pickle.load(f)
                print(f"{book_id}       {mb.title}      {mb.content}     {mb.author}     {mb.createdAt}      {mb.updatedAt}")
                return mb
        else:
            print("Book Not Found")
            return False
    def restore_book(self):
        book_id = input("Enter the Book ID you want to restore(eg:10001) : ")
        if os.path.exists(f"{self.__del_path}{book_id}"):
            shutil.move(f"{self.__del_path}{book_id}",f"{self.__active_path}{book_id}")
        else:
            print("The Book does not exist")
    def confirm_check(self):
        return input("Are you sure. The Action cannot be revert if say yes (Y/N) : ")