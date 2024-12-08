with open('Day-2.txt', 'r') as file:
  input = file.read()
  splitLines = input.split('\n')
  
def checkRange(nums, allowedRange, dampner):
  prev = nums[0]
  for curr in nums[1:]:
    if curr - prev in allowedRange:
      prev = curr
    elif not dampner:
      return False
    else:
      dampner = False
  return True

def isReactorSafe(report):
  nums = [int(num) for num in report.split()]
  increasing = range(1, 4)
  decreasing = range(-3, 0)
  return any([
    checkRange(nums, increasing, True),
    checkRange(nums, decreasing, True),
    checkRange(nums[1:], increasing, False),
    checkRange(nums[1:], decreasing, False)
  ])
  

count = 0
for reportIndex, report in enumerate(splitLines):
  if isReactorSafe(report):
    count += 1

print(count)
