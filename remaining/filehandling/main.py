from file import Filehandling

def menu():
    opt = input("""
1- Write into File
2- Read into File
3- Append to File
4- Exit
""")
    return int(opt)


filename = input("Enter the name of file you want to create : ")
f1 = Filehandling(filename=filename)
option = menu()
while option != 4:
    
    if option == 1:
        data = input("Enter the data to write : ")
        f1.write_to_file(data)
        option = 0
    elif option == 2:
        print(f1.read_file())
        option = 0
    elif option == 3:
        data = input("Enter data to append : ")
        print(f1.append_to_file(data))
        option = 0
    option = menu()