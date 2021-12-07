from lib import *
import re
import math


def calculatefuel(startingpos, endpos):
    return abs(startingpos - endpos)


def middle_element(lst):
    if len(lst) % 2 != 0:
        return lst[int(len(lst) / 2)]
    else:
        return (((lst[int(len(lst) / 2)]) + (lst[int(len(lst) / 2) - 1])) / 2)


def mean(list):
    mean = sum(list) / len(list)
    return math.floor(mean), math.ceil(mean)


def gausSum(n):
    return ((n ** 2) + n) // 2


# File I/O
input = input_as_string("input7.txt")
numbers = list(map(int, re.findall(r'(\d+)', input)))

# Part 1
# find middle element of list
numbers.sort()
target = int(middle_element(numbers))

fuel = 0
# Calculate all the fuel needed
for i in range(len(numbers)):
    fuel += calculatefuel(numbers[i], target)

print(fuel)

# Part 2
fuelfloor = 0
fuelceil = 0

meanfloor, meanceil = mean(numbers)

for i in range(len(numbers)):
    fuelfloor += gausSum(calculatefuel(numbers[i], meanfloor))
    fuelceil += gausSum(calculatefuel(numbers[i], meanceil))

print(min(fuelceil, fuelfloor))
