violator_songs = [['World in My Eyes', 4.86], ['Sweetest Perfection', 4.43],['Personal Jesus', 4.56], ['Halo', 4.9], ['Waiting for the Night', 6.07], ['Enjoy the Silence', 4.20], ['Policy of Truth', 4.76],   ['Blue Dress', 4.29], ['Clean', 5.83]]
time = 0
like_songs = int(input('Сколько песен интересует? '))
song = input(' Название песни? ')

for _ in range(len(violator_songs)):
    if song in violator_songs[_][0]:
        print("Название", _ + 1, "песни: ", violator_songs[_][0])
        time += violator_songs[_][1]


print("Общее время звучания песен: " , time ,"минут")

