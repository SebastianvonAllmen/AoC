from lib import *
import numpy as np


list = input_as_lines("input3.txt")

counter = 0

gamma = []
epsilon = []

for j in range(12):
    for i in range(len(list)):
        if list[i][j] == '0':
            counter += 1
    if counter > len(list)/2:
        gamma.append('0')
    else:
        gamma.append('1')
    counter = 0

for i in range(12):
    if gamma[i] == '0':
        epsilon.append('1')
    else:
        epsilon.append('0')


epsilond = int(''.join(epsilon), 2)
gammad = int(''.join(gamma), 2)

print(epsilond * gammad)
