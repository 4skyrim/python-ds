# TODO здесь писать код
old_list = [3070, 2060, 3090, 3070, 3090 ]
new_list = []
max_number = max(old_list)
for i in old_list:
    if i != max_number:
        new_list.append(i)
print(new_list, ' - the new list of videocards')


