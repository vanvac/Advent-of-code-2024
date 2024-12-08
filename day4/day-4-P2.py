with open("./day4/day-4.txt", 'r') as file:
  puzzleInput = file.read()
  puzzleInput = puzzleInput.split('\n')

def indexAFromInput(puzzleInput):
  aIndexList = []
  for y, line in enumerate(puzzleInput):
    for x, char in enumerate(line):
      if char == 'A':
        aIndexList.append([y, x])
  return aIndexList

def findXMas(startIndex, puzzleInput):
  startY, startX = startIndex
  A = puzzleInput[startY][startX]
  try:
    if startX-1 < 0 or startY -1 <0:
      raise IndexError
    upLeft = puzzleInput[startY-1][startX-1]
  except IndexError:
    upLeft = None

  try:
    if startY-1 < 0:
      raise IndexError
    upRight = puzzleInput[startY-1][startX+1]
  except IndexError:
    upRight = None

  try:
    downRight = puzzleInput[startY+1][startX+1]
  except IndexError:
    downRight = None

  try:
    if startX-1 < 0:
      raise IndexError
    downLeft = puzzleInput[startY+1][startX-1]
  except IndexError:
    downLeft = None

  listOfMandX = [upLeft, upRight, downRight, downLeft]
  resultCount = 0
  for index, char in enumerate(listOfMandX):
    S = listOfMandX[index-2]
    if char == 'M' and S == 'S':
      resultCount += 1
  if resultCount > 1:
    return 1
  else:
    return 0

def findAllXMas(aIndexList, puzzleInput):
  XMasCounter = 0
  for item in aIndexList:
    XMasCounter += findXMas(item, puzzleInput)

  print(XMasCounter)

findAllXMas(indexAFromInput(puzzleInput), puzzleInput)