#Три приятеля были свидетелями нарушения правил дорожного движения. Номер автомобиля - четырехзначное число - никто не  запомнил. Из  их  показаний следует, что номер делиться на 2, на 7 и на 11, в записи номера участвуют только две цифры,  сумма цифр номера  равна  30.  Составьте алгоритм для определения номера автомашины.

def isDivisor(num, div):
  return True if num % div == 0 else False

def countNum(num):
  count = 0
  for n in range(0, 10):
    if str(n) in str(num): count += 1
  return count

def sumNum(num):
  sum = 0
  while num > 10:
    sum += num % 10
    num //= 10
  sum += num
  return sum

for n in range(1000, 10000):
  if isDivisor(n, 2) and isDivisor(n, 7) and isDivisor(n, 11) and countNum(n) == 2 and sumNum(n) == 30:
    print('The required car number is', n)
