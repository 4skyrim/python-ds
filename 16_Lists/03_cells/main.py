N =int(input('Enter the number of cells '))
list_n = []
count = 0

for i in range(1, N):
    list_n.append(i)
length = len(list_n)
for n in range(length):
    if list_n[n] < count:
        print(list_n[n])
    count += 1









