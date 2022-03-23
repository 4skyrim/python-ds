start = int(input('enter number '))
end = int(input(' enter number '))
for number in range(start, end + 1):
    str_number = str(number)
    if (str_number[0] == str_number[1] == str_number[2]  or str_number[0] == str_number[2] == str_number[3] or str_number[1] == str_number[2] == str_number[3]) and not (str_number[0] == str_number[1] == str_number[2] == str_number[3]):
         print(str_number)



