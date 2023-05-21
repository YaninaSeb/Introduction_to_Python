# Найти самое часто встречаемое слово в строке( если оно не одно, самое длинное часто встречаемое слово)
# Найти самое редко встречаемое слово в строке( если оно не одно, самое короткое редко встречаемое слово).
# Заменить каждое найденное часто встречаемое слово на редко встречаемое и наоборот. Вывести полученную строку

def removePunctuationMarks(str):
  punctuationMarks = '.,?!:;-(){}[]'
  newStr = ''

  for item in str:
    if item not in punctuationMarks:
      newStr += item

  return newStr


def sortWords(words):
  words.sort(key=len)
  return words


def getMostFrequentWord(words):
  count = 1
  frequentlyWords = []
  
  for word in words:
    if words.count(word) > count:
      count = words.count(word)
  
  for word in words:
    if words.count(word) == count:
      frequentlyWords.append(word)

  return sortWords(frequentlyWords)[-1]


def getMostRareWord(words):
  count = words.count(words[0])
  rareWords = []
  
  for word in words:
    if words.count(word) < count:
      count = words.count(word)
  
  for word in words:
    if words.count(word) == count:
      rareWords.append(word)

  return sortWords(rareWords)[0]


def replaceWordsInStr(str):
  words = removePunctuationMarks(str).split(' ')
  frequentWord = getMostFrequentWord(words)
  rareWord = getMostRareWord(words)

  for index, word in enumerate(words):
    if word == frequentWord:
      words[index] = rareWord
    elif word == rareWord:
      words[index] = frequentWord

  newStr = ' '.join(words)

  print('The most frequent word is', frequentWord.upper(), 'and the most rare word is', rareWord.upper())
  print('String after replacing these words:', newStr)


str = input('Please, enter a string\n')
replaceWordsInStr(str)
