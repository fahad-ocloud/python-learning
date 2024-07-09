number_words ={
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four"
}
phone  = input("Phone  = ")
words = ""
for value in phone:
    words += number_words.get(value)
print(words)