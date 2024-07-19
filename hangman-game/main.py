from menu import main_menu
from draw_hangman import draw_hanged_man
from hangman import Hangman


def main():
    val,n=0,6
    while True:
        hang = Hangman("")
        val = main_menu()
        hang.pick_word()
        if val>=2:
            break
        while n>0:
            if len(hang.result) == len(hang.guess_word):
                print("Congratulations! you won the game")
                break
            hang.show(n)
            hang.input_character()
            found = hang.ch_found()
            if not found:
                n-=1
                draw_hanged_man(6-n)
        else:
            print(f"You lose! 😔\nThe letter was {hang.guess_word}") 
            n=6       
    else:
        print("Thank you!")
main()