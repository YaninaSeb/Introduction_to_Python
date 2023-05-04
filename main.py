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
