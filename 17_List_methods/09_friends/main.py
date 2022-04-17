freinds_number = int(input('Введите кол-во друзей: '))
loan_note = int(input('Введите количество долговых расписок: '))
friends_list = []
for _ in range(freinds_number):
    friends_list.append(_)

for note in range(loan_note):
    print( note + 1, "расписка: ")
    from_who = int(input("От кого: "))
    to_who = int(input("Кому: "))
    how_much = int(input("Сколько: "))
    friends_list[from_who - 1] += how_much
    friends_list[to_who - 1] -= how_much

print("Баланс друзей: ")
for index in range(len(friends_list)):
    print(index + 1, ": ", friends_list[index])

