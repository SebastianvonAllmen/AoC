from lib import *
import re

data = []
counter = 0

#this shows which segments have to be active for a certain number sevensegg[0] == 1 etc.
sevenseg = [[0, 1, 1, 0, 0, 0, 0],
            [1, 0, 1, 1, 0, 1, 1],
            [1, 1, 1, 1, 0, 0, 1],
            [0, 1, 1, 0, 1, 0, 1],
            [1, 1, 0, 1, 1, 0, 1],
            [1, 1, 0, 1, 1, 1, 1],
            [0, 1, 1, 1, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 0, 1],
            [1, 1, 1, 1, 1, 1, 0]]

def deletepos (possibilty, preservedvalue):
    for i in range(len(possibilty)):
        if i in preservedvalue:
            continue
        possibilty[i] = 0
    
    return possibilty

def remove (possibilty, indexes):
    for i in indexes:
        possibilty[i] = 0
    
    return possibilty


def findvalids (string, possibilities):
    indexs = []
    for i in range(len(string)):
        indexs.append(ord(string[i]) - ord('a'))

    if len(string) == 2:
        deletepos(possibilities[1], indexs)
        deletepos(possibilities[2], indexs)
        remove(possibilities[0], indexs)
        remove(possibilities[3], indexs)
        remove(possibilities[4], indexs)
        remove(possibilities[5], indexs)
        remove(possibilities[6], indexs)

    if len(string) == 4:
        deletepos(possibilities[1], indexs)
        deletepos(possibilities[2], indexs)
        deletepos(possibilities[6], indexs)
        deletepos(possibilities[4], indexs)
        remove(possibilities[0], indexs)
        remove(possibilities[3], indexs)
        remove(possibilities[5], indexs)
    
    if len(string) == 3:
        deletepos(possibilities[1], indexs)
        deletepos(possibilities[2], indexs)
        deletepos(possibilities[3], indexs)
        remove(possibilities[0], indexs)
        remove(possibilities[4], indexs)
        remove(possibilities[5], indexs)
        remove(possibilities[6], indexs)
 
    return possibilities

def setinstone (possibilities, wire, segment):
    for i in range(7):
        possibilities[segment][i] = 0
    for i in range(7):
        possibilities[n][wire] = 0

    possibilities[segment][wire] = 1


#File io
lines = input_as_lines("input8.txt")
for i in range(len(lines)):
    data.append(re.findall("(\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) | (\w+) (\w+) (\w+) (\w+)", lines[i]))

solution = 0

for i in range(len(lines)):
    possibilities = [[1 for j in range(7)] for i in range(7)]
    stringsix = []
    stringfive = []
    for j in range(10):
        #This narrows down all the possible solutions with the easy to find digits
        findvalids(data[i][0][j], possibilities)

        if len(data[i][0][j]) == 6:
            stringsix.append(data[i][0][j])
        
        if len(data[i][0][j]) == 5:
            stringfive.append(data[i][0][j])

    #now we look for the cable that goes bottom right field, that would be index 1 of the possibility list
    wireBoRi = []
    for n in range(len(possibilities)):
        if possibilities[1][n] == 1:
            wireBoRi.append(n)

    charBoRi = chr(wireBoRi[0] + ord('a'))
    ctrBoRi = 0

    for n in range(3):
        ctrBoRi += stringsix[n].count(charBoRi)

    if ctrBoRi == 2:
        setinstone(possibilities, wireBoRi[0], 2)
        setinstone(possibilities, wireBoRi[1], 1)
    else:
        setinstone(possibilities, wireBoRi[1], 2)
        setinstone(possibilities, wireBoRi[0], 1)

    
    #Now we need to figure out which one goes top left
    wireToLe = []

    for n in range(len(possibilities)):
        if possibilities[4][n] == 1:
            wireToLe.append(n)
    
    charToLe = chr(wireToLe[0] + ord('a'))
    ctrToLe = 0

    for n in range(3):
        ctrToLe += stringfive[n].count(charToLe)

    if ctrToLe == 1:
        setinstone(possibilities, wireToLe[0], 4)
        setinstone(possibilities, wireToLe[1], 6)
    else:
        setinstone(possibilities, wireToLe[1], 4)
        setinstone(possibilities, wireToLe[0], 6)
    
    #Now we only need to identify the bottom left field
    wireBoLe = []

    for n in range(len(possibilities)):
        if possibilities[5][n] == 1:
            wireBoLe.append(n)

    charBoLe = chr(wireBoLe[0] + ord('a'))
    ctrBoLe = 0

    for n in range(3):
        ctrBoLe += stringfive[n].count(charBoLe)

    if ctrBoLe == 1:
        setinstone(possibilities, wireBoLe[0], 5)
        setinstone(possibilities, wireBoLe[1], 0)
    else:
        setinstone(possibilities, wireBoLe[1], 5)
        setinstone(possibilities, wireBoLe[0], 0)

    #Now we finally get to the fun part of calculating our number
    code = 0
    for j in range(10,14):
        currentseg = [0] * 7
        for n in range(len(data[i][1][j])):
            charindex = ord(data[i][1][j][n]) - ord('a')
            charseg = 0
            for m in range(7):
                charseg = m
                if(possibilities[m][charindex] == 1):
                    break
            
            currentseg[charseg] = 1
        
        number = (sevenseg.index(currentseg) + 1) % 10
        code += number * (10 ** (13-j))
    
    solution += code


print("The sum is", solution)