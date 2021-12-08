from lib import *
import re

data = []
counter = 0

def deletepos (possibilty, preservedvalue):
    for i in range(len(possibilty)):
        if i in preservedvalue:
            continue
        possibilty[i] = 0
    
    return possibilty

def possibilities (string, possibilities):
    indexs = []
    for i in len(string):
        indexs.append(ord(string[i]) - ord('a'))

    if len(string) == 2:
        deletepos(possibilities[1], indexs)
        deletepos(possibilities[2], indexs)

    if len(string) == 
        
    
    return possibilities




#File io
lines = input_as_lines("input8.txt")
for i in range(len(lines)):
    data.append(re.findall("(\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) | (\w+) (\w+) (\w+) (\w+)", lines[i]))

for i in range(len(lines)):
    possibilities = [[1 for j in range(7)] for i in range(7)]
    for j in range(0,14):
        if j > 9:
            data[i][1][j]
        else:
            data[i][0][j]


print(counter)