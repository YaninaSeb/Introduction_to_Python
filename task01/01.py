#Представить десятичное целое число в двоичном виде

try:
  num = int(input('Please, enter a decimal number: '))
  
  def changeNum(n):
    if n == 0: 
      return 0
    else: 
      binary = ''
      while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
      return int(binary)

  binaryNum = changeNum(abs(num))
  if num < 0: binaryNum = -binaryNum
  print('Decimal number', num, 'in binary is', binaryNum)

except ValueError:
  print('The entered data is incorrect')
