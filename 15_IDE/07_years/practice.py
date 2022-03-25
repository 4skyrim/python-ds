ask =int( input('Сколько сотрудников в офисе? '))
list = []
for i in range(0, ask):
    id_num = int(input('Введите id '))
    list.append(id_num)
employee_ask = int(input('Введите номер интерисующего вас сотрудника '))
print(employee_ask in list)