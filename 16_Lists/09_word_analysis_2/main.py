
word = list(input('enter word '))
rev_word = []
for elem in reversed(word):
     rev_word.append(elem)
if rev_word == word:
    print('palindrome ')
else:
    print('no palindrome')
