def splitInputIntoLists(inputString):
  list1, list2 = ([], [])
  for line in inputString.splitlines():
    split = line.split(' ')
    list1.append(int(split[0]))
    list2.append(int(split[3]))
  return list1, list2


def compareLists(listA, listB):
  listA.sort()
  listB.sort()
  diff = 0
  for index, item1 in enumerate(listA):
    diff += abs(item1 - listB[index])
  return diff

def findSimilar(listA, listB):
  result = 0
  for number in listA:
    howMany = listB.count(number)
    result += number * howMany
  return result

with open("Day-1.txt", "r") as file:
  a, b = splitInputIntoLists(file.read())

print(compareLists(a, b))
print(findSimilar(a,b))
