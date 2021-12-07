from lib import *
import re

def calculatefuel (startingpos, endpos):
    return abs(startingpos - endpos)

def middle_element(lst):
  if len(lst) % 2 != 0:
    return lst[int(len(lst) / 2)]
  else:
    return (((lst[int(len(lst) / 2)]) + (lst[int(len(lst) / 2) - 1])) / 2)

input = input_as_string("input7.txt")
numbers = list(map(int, re.findall(r'(\d+)', input)))

#find most commen element of list
fuel = 0

numbers.sort()
target = int(middle_element(numbers))

#Calculate all the fuel needed
for i in range(len(numbers)):
    fuel += calculatefuel(numbers[i], target)

print(fuel)