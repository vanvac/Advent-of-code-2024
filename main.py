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


with open("input.txt", "r") as file:
  a, b = splitInputIntoLists(file.read())

print(compareLists(a, b))
