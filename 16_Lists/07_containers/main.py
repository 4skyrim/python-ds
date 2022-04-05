number = int(input('Enter the number of boxes '))
for _ in range(number):
    ask = int(input('Enter the weight of the box '))
    if ask > 200:
        print('Error. Number cannot be greater than 200 and cannot be float. Try again. ')
        ask = int(input('Enter the weight of the box '))

new_box = int(input('enter weight '))


