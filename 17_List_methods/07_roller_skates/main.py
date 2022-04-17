scates = int(input('Кол-во коньков: '))
size = []
foot = []
for i in range(scates):
    a = int(input('Размер пары: '))
    print('Размер ', i + 1, 'пары коньков', a)
    size.append(a)

people = int(input('Количество людей: '))
for i in range(people):
    b = int(input('Размер ноги  человека: '))
    print('Размер ноги ', i + 1, 'человека ', b)
    foot.append(b)

match = 0
for foot_ind in range(people):
    for shoes_ind in range(scates):
        if foot[foot_ind] <= size[shoes_ind]:
            match += 1
print('Наибольшее число людей с роликами: ', match)

# for shoes_ind in range(scates):
#     for foot_ind in range(people):



