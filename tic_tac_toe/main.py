from tictactoe import Tictactoe
def main_menu():
    return input("""
1-Start Game
2-Exit

choose your Option : """)
def main():
    while True:
        option = main_menu()
        
        x=0
        match int(option):
            case 1:
                size = int(input("Enter the Board size : "))
                g1 = Tictactoe(size)
                g1.sample_board()
                print("\n\n")
                g1.game_board()
                while True:
                    location = int(input(f"Choose your location Player : {'X' if x%2 == 0 else 'O'} for entry : "))
                    print(location,size)
                    if location>0 and location<=size*size:
                        if g1.add_value(location, 'X' if x%2 == 0 else 'O'):
                            x+=1
                        else:
                            print("###########Already Filled#########")
                        result = g1.check_winner('O' if x%2 == 0 else 'X')
                        g1.sample_board()
                        print("\n\n")
                        g1.game_board()
                        if result=='X' or result == 'O':
                            print(f"`{result}` wins")
                            break
                        if x == size*size:
                            print("Draw!")
                            break
                    else:
                        print("Invalid entry") 
            case 2:
                break
            case _:
                print("Invalid Option")
main()