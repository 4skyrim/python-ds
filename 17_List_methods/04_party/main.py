def party(guests):

 capacity = len(guests)
 while True:
     print('Number of guests: ', len(guests), 'Guests: ', guests)
     ask  =input(' come or leave? ')

     if  capacity < 6:
         if ask == 'come':
             capacity += 1
             name = input('Who is it? ')
             guests.append(name)
         elif ask == 'leave':
            capacity -= 1
            name = input('Who is it?')
            guests.remove(name)
     if capacity > 6:
        print('Too much. Go away ')
        print('Number of guests: ', len(guests), 'Guests: ', guests)
        ask = input(' come or leave? ')

     if ask == 'sleep':
      break

guests = ['Kate', 'Boris', 'Jake', 'Vah', 'Tori']

party(guests)