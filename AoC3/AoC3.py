import copy
from lib import *
import numpy as np


def find_most_common(input, index):
    entry = [a[index] for a in input]
    one = entry.count("1")
    zero = entry.count("0")
    if one >= zero:
        return '1'
    else:
        return '0'


list = input_as_lines("input3.txt")

# Init data
gamma = []
epsilon = []

# find gamma
for i in range(12):
    mstc = find_most_common(list, i)
    gamma.append(mstc)

# find epsilon
for i in range(12):
    if gamma[i] == '0':
        epsilon.append('1')
    else:
        epsilon.append('0')


# Convert to dec
epsilond = int(''.join(epsilon), 2)
gammad = int(''.join(gamma), 2)

# output of first quiz
print(epsilond * gammad)

# Start of second part
# find oxygenrat
oxygenrat = copy.copy(list)
co2rat = copy.copy(list)

for i in range(12):
    if len(oxygenrat) == 1:
        break

    mstc = find_most_common(oxygenrat, i)

    if mstc == '0':
        oxygenrat.sort()

        # delete rest
        for index in range(len(oxygenrat)):
            if(oxygenrat[index][i] == '1'):
                del oxygenrat[index:]
                break

    if mstc == '1':
        oxygenrat.sort(reverse=True)
        index = 0

        # delete stuff
        for index in range(len(oxygenrat)):
            if(oxygenrat[index][i] == '0'):
                del oxygenrat[index:]
                break

# find co2 rating
for i in range(12):
    if len(co2rat) == 1:
        break

    # Find the left most commen
    mstc = find_most_common(co2rat, i)
    lstc = ''

    # lstc has to be opposite of mstc
    if mstc == '1':
        lstc = '0'
    else:
        lstc = '1'

    # delete all the 0
    if lstc == '0':
        co2rat.sort()

        for index in range(len(co2rat)):
            if(co2rat[index][i] == '1'):
                del co2rat[index:]
                break

    # Delete all the 0
    if lstc == '1':
        co2rat.sort(reverse=True)

        for index in range(len(co2rat)):
            if(co2rat[index][i] == '0'):
                del co2rat[index:]
                break

# convert to decimal
co2d = int(''.join(co2rat), 2)
oxyd = int(''.join(oxygenrat), 2)

print(co2d * oxyd)
