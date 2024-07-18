from menu import main_menu
from draw_hangman import draw_hanged_man
import random
def pick_word():
    with open("words.txt","r") as f:
        return random.choices(f.readlines()) 
def ch_found(guess_word,guess_ch,result):
    x=0
    while x<len(guess_word):
        if guess_ch in result:
            return False
        if guess_ch == guess_word[x]:
            return True
        x+=1
def show(n,guess_word,result):
    print(f"You have Only {n} guesses left!")
    s=""
    for x in guess_word:
        current = x
        if x in result:
            s+=f"{x} "
        else:
            s+="_ "
    print(s)
def main():
    result=""
    val,n=0,6
    while val!=2:
        val = main_menu()
        guess_word =pick_word()[0][0:-1]
        while n>0:
            if len(result) == len(guess_word):
                print("Congratulations! you won the game")
                break
            show(n,guess_word,result)
            guess_ch = input("Enter the any character which is present in following hint : ")
            found = ch_found(guess_word,guess_ch,result)
            if not found:
                n-=1
                draw_hanged_man(6-n)
            else:
                result+=guess_ch         
    else:
        print("Thank you!")
main()