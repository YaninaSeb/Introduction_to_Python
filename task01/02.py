#Бактерии бывают двух видов - черные и белые. Черная бактерия за каждый такт делится на 2 черные и 1 белую, белая - на 1 черную и 1 белую. Выяснить сколько бактерий каждого вида будет после T тактов, если на первом такте было А - белых и В - черных .

try:
  countWhite = int(input('Please, enter the number of white bacteria: '))
  countBlack = int(input('Please, enter the number of black bacteria: '))
  countTact = int(input('Please, enter the number of tact: '))

  if countWhite < 0 or countBlack < 0 or countTact <= 0: raise ValueError

  def changeCount(countW, countB, tact):
    if tact == countTact:
      return countW, countB
    else:
      newCountW = countW + countB
      newCountB = countW + countB * 2
      tact += 1
      return changeCount(newCountW, newCountB, tact)

  countWhite, countBlack = changeCount(countWhite, countBlack, 1)
  print('After', countTact, "cycles the number of white bacteria is", countWhite, 'and the number of black bacteria is', countBlack)

except ValueError:
  print('The entered data is incorrect!')
