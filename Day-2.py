with open('Day-2.txt', 'r') as file:
  input = file.read()
  splitLines = input.split('\n')
  seperatedNumbers = []
  for line in splitLines:
    seperatedNumbers.append(line.split(' '))

def isDiffSafeAndDecrease(previous, current):
  diff = int(previous)-int(current)
  decreasing = None

  if abs(diff) == diff: decreasing = True 
  else: decreasing = False

  if diff <= 3 or diff >= 1: diff = True #checks if the difference is safe
  else: diff = False

  return diff, decreasing

def isSafeReactor(report):
  isReportDecreasing = None
  for index in range(1, len(report)):
    safeDiff, decreasing = isDiffSafeAndDecrease(report[index-1], report[index])

    if isReportDecreasing is None:
      isReportDecreasing = decreasing

    if safeDiff == False:
      return False
    
    if isReportDecreasing != decreasing:
      return False
    
    return True
    
def findSafeReactorAmount(reports):
  for report in reports:
    safeReactorCount = 0
    if isSafeReactor(report): safeReactorCount += 1
  return safeReactorCount

print(findSafeReactorAmount(seperatedNumbers))