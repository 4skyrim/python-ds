list_1 = []
list_2 = []

for i in range(3):
    c = int(input('Enter  number '))
    list_1.append(i)

print('list 1: ', list_1)

for a in range(7):
    b = int(input('Enter number ',))
    list_2.append(a)

print('list 2: ', list_2 )

list_1.extend(list_2)
list_1 = list(set(list_1))
print('cleared list: ', *list_1)




