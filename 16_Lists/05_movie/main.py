films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']

fav_list = []
while True:
    ask_fav = input(' Name ur fav film. If u want to end print "stop" ')
    if ask_fav in films:
        fav_list.append(ask_fav)
        print('film added')
    elif ask_fav == 'stop' or ask_fav == 'Stop':
        break
    else:
        print('Error. Ur film is not in list. Try another one ')


print(fav_list)

