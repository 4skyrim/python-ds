
unique_letter = 0
word = input('enter word ')
count = 0
for letter in word:
    word.count(letter)
    if  word.count(letter) == 1:
        unique_letter += 1
print(unique_letter)