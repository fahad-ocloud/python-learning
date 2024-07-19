from library_pk.library import Library
def menu():
    return int(input("""
1-Add new book
2-Delete a Book
3-View Books
4-Update Book
5-Search Book
6-View Delete History  
7-Exit

Select any option: """))
    
def nest_menu():
     return int(input("""
1-Permanently Delete book
2-Restore
3-Back

Select any option: """))
def main():
    l1=Library()
    while True:
        option = menu()
        match option:
            case 1:
                title = input("Enter the Title of the Book : ")
                author = input("Enter the Author of the Book : ")
                content = input("Enter the Content of the Book : ")
                l1.add_new_book(title,content,author)
            case 2:
                book_id = input("Enter the Book ID you want to Delete(eg:10001) : ")
                l1.del_book(book_id)
            case 3:
                l1.view_book(True)
            case 4:
                book_id = input("Enter Book ID you want update(eg:10001) : ")
                flag = l1.search_book(book_id)
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
                    l1.update_book(book_id,title,content,author,flag.createdAt)
            case 5:
                book_id = input("Enter Book ID you want search(eg:10001) : ")
                l1.search_book(book_id)
            case 6:
                while True:
                    l1.view_book(False)
                    nest_option = nest_menu() 
                    match nest_option:
                        case 1:
                            book_id = input("Enter the Book ID you want to Permanently DELETE(eg:10001) : ")
                            l1.permanent_del_book(book_id)
                        case 2:
                            l1.restore_book()
                        case 3:
                            break
            case 7:
                break
            case _:
                print("Invalid Entry")
                
main()         