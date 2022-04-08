
list_box = [160,  160, 157]
new = int(input('Введите вес '))

position = 0

while position < len(list_box) and list_box[position] >= new:
    position += 1

print('Номер, куда встанет новый контейнер:', position + 1)