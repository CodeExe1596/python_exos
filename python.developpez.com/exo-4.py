word = input("Please enter a word and we'll try to make a pyramid with it : \n")

while " " in word:
    print("Please enter a single word with no brackets !")
    word = input("Please enter a word and we'll try to make a pyramid with it : \n")

i = 1

while i <= len(word):
    print(word[:i])
    word = word[i:]
    i += 1