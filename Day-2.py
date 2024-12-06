with open('Day-2.txt', 'r') as file:
  input = file.read()
  splitLines = input.split('\n')
  seperatedNumbers = []
  for line in splitLines:
    seperatedNumbers.append(line.split(' '))

