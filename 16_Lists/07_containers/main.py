list_box = [170, 168, 167, 160]
position = 0
for i in list_box:
    new = int(input('Enter weight: '))
    if new <= i:
        position += 1

list_box.insert(position, new)

print(list_box)

