list_1 = []
list_2 = []
for i_list in range(160, 170, 2):
    list_1.append(i_list)
for j_list in range(162,180, 3):
    list_2.append(j_list)
list_2.extend(list_1)
list_2.sort()
print(' sorted list: ', list_2)
