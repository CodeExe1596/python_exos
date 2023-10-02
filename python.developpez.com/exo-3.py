phrase = input("Please enter a phrase and we'll try to reverse it : \n")

newPhrase = ''

for i in range(0, len(phrase)):
    newPhrase += phrase[len(phrase) - i - 1]

print("Your reversed phrase : ", newPhrase)
