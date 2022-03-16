
n = int(input('enter number '))
def summ(n):
    summ = 0
    while n != 0:
        summ += n %10
        n //= 10
    print('sum of digits', summ)
    return(n)
def count(n):
    count = 0
    while n != 0:
        count += 1
        n //= 10
    print('amount of digits ', count)
    return(n)
summ(n)
count(n)




