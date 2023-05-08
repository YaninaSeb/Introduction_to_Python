# # TASK 1
# # Найти количество гласных букв в строке введенной пользователем
# str = input('Please, enter the string\n')
# str = str.lower()
# count = 0
# for letter in str:
#   if letter in ['a', 'e', 'i', 'o', 'u', 'y']:
#     count += 1
# print('number of vowels in a string is', count, '\n')

# # TASK 2
# #Найти сумму цифр числа
# num = input('Please, enter the number\n')
# num = abs(int(num))
# sum = 0
# while num > 10:
#   sum += num % 10
#   num //= 10
# sum += num
# print('The sum of the digits of a number', sum, '\n')

# # TASK 3
# #Номер билета состоит из 7 цифр. Проверить является ли билет счастливым (цифры слева-направо и справа-налево стоят в одинаковом порядке)
# num = int(input('Please, enter the number\n'))
# currentNum = num
# newNum = 0

# while currentNum > 10:
#   newNum = newNum * 10 + currentNum % 10
#   currentNum //= 10

# newNum = newNum * 10 + currentNum % 10

# if newNum == num:
#   print('This ticket is lucky\n')
# else:
#   print('This ticket is not lucky\n')


# # TASK 4
# #Проверить является ли число N совершенным
# num = int(input('Please, enter the number\n'))
# divider = 1
# sumDividers = 0

# if num <= 0:
#   print('number', num, 'is not perfect\n')

# while divider <= num / 2:
#   if num % divider == 0:
#     sumDividers += divider
#   divider += 1

# if sumDividers == num:
#   print('number', num, 'is perfect\n')
# else:
#   print('number', num, 'is not perfect\n')


# # TASK 5
# #Проверить являются ли числа А и В взаимнопростыми.
# numA = int(input('Please, enter the positive num A\n'))
# numB = int(input('Please, enter the positive num B\n'))
# divider = 1
# sumDividers = 0

# while divider <= numA:
#   if numA % divider == 0 and numB % divider == 0:
#     print(divider)
#     sumDividers += divider
#   divider += 1

# if sumDividers == 1:
#   print('numbers', numA, 'and', numB, 'are coprime\n')
# else: 
#   print('numbers', numA, 'and', numB, 'are not coprime\n')


# # TASK 6
# #Представить десятичное целое число в двоичном виде
# print('Please, enter a decimal number:')
# num = int(input())
# binaryNum = ''

# def changeIntPart(n):
#   intPart = ''
#   while n > 0:
#     intPart = str(n % 2) + intPart
#     n = n // 2
#   return intPart

# binaryNum = changeIntPart(num) or 0
# print('Decimal number', num, 'in binary is', binaryNum)


# # TASK 11
# #Бактерии бывают двух видов - черные и белые. Черная бактерия за каждый такт делится на 2 черные и 1 белую, белая - на 1 черную и 1 белую. Выяснить сколько бактерий каждого вида будет после T тактов, если на первом такте было А - белых и В - черных .
# countWhite = int(input('Please, enter the number of white bacteria: '))
# countBlack = int(input('Please, enter the number of black bacteria: '))
# countTakt = int(input('Please, enter the number of takt: '))

# def changeCount(countW, countB, takt):
#   if takt == countTakt:
#     return countW, countB
#   else:
#     newCountW = countW + countB
#     newCountB = countW + countB * 2
#     takt += 1
#     return changeCount(newCountW, newCountB, takt)

# countWhite, countBlack = changeCount(countWhite, countBlack, 1)
# print('After', countTakt, "cycles the number of white bacteria is", countWhite, ',the number of black bacteria is', countBlack)


# # TASK 12
# #Три приятеля были свидетелями нарушения правил дорожного движения. Номер автомобиля - четырехзначное число - никто не  запомнил. Из  их  показаний следует, что номер делиться на 2, на 7 и на 11, в записи номера участвуют только две цифры,  сумма цифр номера  равна  30.  Составьте алгоритм для определения номера автомашины.

# def isDivisor(num, div):
#   return True if num % div == 0 else False

# def countNum(num):
#   count = 0
#   for n in range(0, 10):
#     if str(n) in str(num): count += 1
#   return count
  
# def sumNum(num):
#   sum = 0
#   while num > 10:
#     sum += num % 10
#     num //= 10
#   sum += num
#   return sum
  
# for n in range(1000, 10000):
#   if isDivisor(n, 2) and isDivisor(n, 7) and isDivisor(n, 11) and countNum(n) == 2 and sumNum(n) == 30:
#     print('The required car number is', n)
