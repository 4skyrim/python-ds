cells_list = [1, 2, 6, 8, 5]
new_list = []
print('Количество клеток: ', len(cells_list))
for i in range(len(cells_list)):
    if  i > cells_list[i]:
        new_list.append(i)

if new_list == []:
    new_list.append('отсутсвуют')

print('Неподходящие значения: ', *new_list)










