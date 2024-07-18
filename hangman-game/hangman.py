import random
class Hangman:
    def __init__(self,result):
        self.result = result
    def pick_word(self):
        with open("words.txt","r") as f:
            self.guess_word = random.choices(f.readlines())[0][0:-1] 
    def input_character(self):
        self.guess_ch = input("Enter the any character which is present in following hint : ")
    def ch_found(self):
        x=0
        while x<len(self.guess_word):
            if self.guess_ch in self.result:
                print("Already Exist")
                return True
            if self.guess_ch == self.guess_word[x]:
                self.result+=self.guess_ch
                return True
            x+=1
    def show(self,n):
        print(f"You have Only {n} guesses left!")
        s=""
        for x in self.guess_word:
            current = x
            if x in self.result:
                s+=f"{x} "
            else:
                s+="_ "
        print(s)