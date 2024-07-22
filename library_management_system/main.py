from library_pk.library import Library
from datetime import datetime
from library_pk.person import Person
from library_pk.display import display_books
def menu():
    return input("""
1-Add new book
2-Delete a Book
3-View Books
4-Update Book
5-Search Book
6-View Delete History  
7-Return the Book
8-Assign the Book
9-View Transactions
10-Exit


Select any option: """)
    
def nest_menu():
     return input("""
1-Permanently Delete book
2-Restore
3-Back

Select any option: """)
def main():
    l1=Library()
    while True:
        option = menu()
        match int(option):
            case 1:
                title = input("Enter the Title of the Book : ")
                author = input("Enter the Author of the Book : ")
                content = input("Enter the Content of the Book : ")
                l1.add_new_book(title,content,author)
            case 2:
                book_id = int(input("Enter the Book ID you want to Delete(eg:10001) : "))
                l1.del_book(book_id-1)
            case 3:
                l1.view_book(True)
            case 4:
                book_id = int(input("Enter Book ID you want update(eg:1) : "))
                flag = l1.search_book(book_id-1)
                if flag:
                    print("If you Press Enter without any entry. It gets the default name..")
                    title = input("Enter the Title of the Book : ")
                    author = input("Enter the Author of the Book : ")
                    content = input("Enter the Content of the Book : ")
                    if title=="":
                        title = flag.title
                    if author=="":
                        author = flag.author
                    if content=="":
                        content=flag.content
                    res = l1.update_book(book_id-1,title,content,author,flag.createdAt, datetime.now())
                    print("############# BOOK Updated #############")
            case 5:
                book_id = int(input("Enter Book ID you want search(eg:10001) : "))
                book = []
                data = l1.search_book(book_id-1)
                if data:
                    book.append(data)
                    display_books(book)
                else:
                    print("!!!!Book not Found!!!!")
            case 6:
                while True:
                    l1.view_book(False)
                    nest_option = nest_menu() 
                    match int(nest_option):
                        case 1:
                            book_id = int(input("Enter the Book ID you want to Permanently DELETE(eg:10001) : "))
                            l1.permanent_del_book(book_id-1)
                        case 2:
                            l1.restore_book()
                        case 3:
                            break
                        case _:
                            print("!!!!!!!!!!Invalid Entry!!!!!!!!!!!!!")
            case 7:
                pid = input("Enter the Person email e.g (fahad@gmail.com) : ")
                name = input("Enter the person name e.g (Fahad Asif) : ")
                p1 = Person(pid,name)
                book_id= int(input("Enter the book id you want to assign eg(1): "))
                found  = l1.search_book(book_id-1)
                if found:
                    if found.borrower_email == pid:   
                        l1.return_book(p1 , found , book_id -1)
                        print(f"###### BOOK Return by {p1.name} ######")
                    else:
                        print("!!!!!!!!!Invalid Person id!!!!!!!!!!!")
                else:
                    print("!!!!!!!!!! Book Not Found !!!!!!!!!")
            case 8:
                pid = input("Enter the Person email e.g (fahad@gmail.com) : ")
                name = input("Enter the person name e.g (Fahad Asif) : ")
                p1 = Person(pid,name)
                book_id= int(input("Enter the book id you want to assign eg(1): "))
                found  = l1.search_book(book_id-1)
                if found:
                    if found.isAvailable:   
                        l1.assign_book(p1 , found , book_id -1)
                        print(f"############# BOOK Assigned to {p1.name} ###########")
                    else:
                        print("!!!!!!!!!!!!!!Book is not available!!!!!!!!!!!!!!")
                else:
                    print("!!!!!!!!!!!!! Book Not Found !!!!!!!!!!!!!!!!!")
            case 9:
                l1.view_Transaction()
            case 10:
                break
            case _:
                print("!!!!!!!!!!Invalid Entry!!!!!!!!!!!!!")
                
main()         