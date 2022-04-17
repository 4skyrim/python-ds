list_1 = []
list_2 = []

for _ in range(3):
    c = int(input('Enter  number '))
    list_1.append(c)

print('list 1: ', list_1)

for _ in range(7):
    b = int(input('Enter number ',))
    list_2.append(b)

print('list 2: ', list_2 )

list_1.extend(list_2)
for elem in list_1:
   count =  list_1.count(elem)
   if count > 1:
       for _ in range(count - 1):
           list_1.remove(elem)

print('cleared list: ', *list_1)





