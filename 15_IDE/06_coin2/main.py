print("Enter coin coordinates:" )
X = float(input('X = '))
Y = float(input('Y = '))
radio = float(input('radio = '))

def radius(X, Y, radio):
    if X > radio or Y> radio:
        print('Coin is not here')
    else:
        print('U are close to coin')

radius(X, Y, radio)


