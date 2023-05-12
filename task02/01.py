# В списке найти среднее арифметическое элементов расположенных между первым максимальным и первым минимальным элементами.

def getMinNumInd(lst):
  minNum = lst[0]
  for n in lst:
    if n < minNum: minNum = n
  return lst.index(minNum)

def getMaxNumInd(lst):
  maxNum = lst[0]
  for n in lst:
    if n > maxNum: maxNum = n
  return lst.index(maxNum)

def getAverage(lst):
  sum = 0
  for n in lst: sum += n
  return sum / len(lst)

def averageValue(list):
  minNumInd = getMinNumInd(list)
  maxNumInd = getMaxNumInd(list)

  if minNumInd > maxNumInd: 
    minNumInd, maxNumInd = maxNumInd, minNumInd

  average = getAverage(nums[minNumInd+1:maxNumInd])

  return average


# example
nums = [1, 8, 2, 4, 6, 8, 3, 10, -2, 1, 0]

print('Average value between the first maximum number and the first minimum number is', averageValue(nums))
