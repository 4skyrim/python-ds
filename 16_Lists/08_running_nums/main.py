
K = int(input('Enter step value '))
print('Shift: ', K)
N = [1, 2, 3, 4, 5]
print(N[-K:] + N[: -K])
