with open("day-4.txt", 'r') as file:
  puzzleInput = file.read()
  puzzleInput = puzzleInput.split('\n')

def indexXFromInput(puzzleInput):
  xIndexList = []
  for y, line in enumerate(puzzleInput):
    for x, char in enumerate(line):
      if char == 'X':
        xIndexList.append([y, x])
  return xIndexList

def findXmas(puzzleInput, startIndex, yIncrement = 0, xIncrement = 0):
  startY, startX = startIndex
  X = puzzleInput[startY][startX]
  try:
    if startY+(yIncrement*1) < 0 or startX+(xIncrement*1) < 0:
      raise IndexError
    M = puzzleInput[startY+(yIncrement*1)][startX+(xIncrement*1)]
  except IndexError:
    return False
  
  try:
    if startY+(yIncrement*2) < 0 or startX+(xIncrement*2) < 0:
      raise IndexError
    A = puzzleInput[startY+(yIncrement*2)][startX+(xIncrement*2)]
  except IndexError:
    return False
  
  try:
    if startY+(yIncrement*3) < 0 or startX+(xIncrement*3) < 0:
      raise IndexError
    S = puzzleInput[startY+(yIncrement*3)][startX+(xIncrement*3)]
  except IndexError:
    return False
  
  xmas = X+M+A+S
  if xmas == 'XMAS':
    return True
  else:
    return False
  
def findAllXMAS(xIndexList, puzzleInput):
  xmasList = []
  counter = 0
  for xIndex in xIndexList:
    up = findXmas(puzzleInput, xIndex, -1, 0)
    upRight = findXmas(puzzleInput, xIndex, -1, +1)
    right = findXmas(puzzleInput, xIndex, 0, +1)
    downRight = findXmas(puzzleInput, xIndex, +1, +1)
    down = findXmas(puzzleInput, xIndex, +1, 0)
    downLeft = findXmas(puzzleInput, xIndex, +1, -1)
    left = findXmas(puzzleInput, xIndex, 0, -1)
    upLeft = findXmas(puzzleInput, xIndex, -1, -1)
    xmasList.append([up, upRight, right, downRight, down, downLeft, left, upLeft])
  for list in xmasList:
    for item in list:
      if item is True:
        counter += 1
  return counter

print(findAllXMAS(indexXFromInput(puzzleInput), puzzleInput))

