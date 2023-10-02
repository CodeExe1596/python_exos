phrase = input("Please write a phrase and we'll add '*' between each letter : \n")

newPhrase = ''

for i in range(0, len(phrase)):
    newPhrase += phrase[i]
    if i < (len(phrase)-1):
        newPhrase += '*'

print("Your new phrase is : ", newPhrase)
