
n = int(input('enter number'))
i = 1
while i <= n:
    i += 1
    if n%i == 0:
        print("наименьший делитель: ",  i)
        break
