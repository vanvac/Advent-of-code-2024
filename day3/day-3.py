with open("day-3.txt", 'r') as file:
  puzzleInput = file.read()

def findMul(puzzleInput):
  mulIndexList = []
  lookForClose = False
  enabled = True
  for index, character in enumerate(puzzleInput):
    if character == 'd':
      if puzzleInput[index:index+4] == 'do()':
        enabled = True
      elif puzzleInput[index:index+7] == "don't()":
        enabled = False
    if character == 'm':
      if puzzleInput[index:index+4] == 'mul(':
        startIndex = index
        lookForClose = True
    if lookForClose and character == ')':
      if index - startIndex <= 11 and enabled:
        mulIndexList.append([startIndex, index])
      lookForClose = False
  return mulIndexList

def findNumbers(mul):
  numbers = []
  nextNum = False
  num = ''
  for char in mul:
    if char == '(':
      nextNum = True
    elif nextNum and char in ',)':
      numbers.append(int(num))
      num = ''
    elif nextNum:
      num += char
  return numbers
def calculateTotal(mulIndexList, puzzleInput):
  total = 0
  for instruction in mulIndexList:

    a, b = findNumbers(puzzleInput[instruction[0]:instruction[1]+1])
    total += a*b
  return total

print(calculateTotal(findMul(puzzleInput), puzzleInput))