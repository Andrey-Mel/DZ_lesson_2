#Задачи на циклы и оператор условия------
#----------------------------------------

'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''
for i in range(5):
    print(str(i+1)+'. 00000')

'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
j = 0
vol_5 = 0
for j in range(10):
    digit_user = input('Введите чило: ')
    j += 1
    if int(digit_user) == 5:
        vol_5 += 1
print('Введено пятерок ' + str(vol_5) + ' р.')
'''
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
sum = 0

for i in range(1,101):
    sum += i
print(sum)

'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''
mult = 1

for i in range(1, 11):
    mult *= i
print(mult)
'''
Задача 5
Вывести цифры числа на каждой строчке.
'''
Выводит последовательно
integer_number = 2927
k = 0
while k < len(str(integer_number)):
    print(str(integer_number)[k])
    k += 1

###print(integer_number % 10, integer_number // 10)
while integer_number>0:
    print(integer_number % 10)
    integer_number = integer_number//10

'''
Задача 6
Найти сумму цифр числа.
'''
int_num = 567654
sum = 0
while int_num != 0:
    sum += int_num % 10
    int_num = int_num // 10
print(sum)

'''
Задача 7
Найти произведение цифр числа.
'''
int_num = 2121
mult = 1
while int_num != 0:
    mult *= int_num % 10
    int_num = int_num // 10
print(mult)
'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
integer_number = 215513
while integer_number:
    if integer_number % 10 == 5:
        print('Yes')
        break
    integer_number = integer_number//10
else: print('No')

'''
Задача 9
Найти максимальную цифру в числе
'''
integer_number = 876821
temp = 0
max_num = 0
while integer_number > 0:
    temp = integer_number % 10
    if temp > max_num:
        max_num = temp
    integer_number = integer_number // 10
print(max_num)

# Или

print(max(str(integer_number)))

'''
Задача 10
Найти количество цифр 5 в числе
'''
integer_num = 5555555555
temp_num = 0
vol_5 = 0
while integer_num !=0:
    temp_num = integer_num % 10
    if temp_num == 5:
        vol_5 += 1
    integer_num = integer_num // 10
print('Введено пятерок ' + str(vol_5) + ' р.')