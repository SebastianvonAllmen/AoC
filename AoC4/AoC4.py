from lib import *
import numpy as np

input = input_as_lines("input4.txt")

#Convert first row in string to numbers
num_order = [int(s) for s in input[0].split(",")]

num_len_input = int((len(input) - 1) / 6)

bingo_boards_str = [[None] * 5 for i in range(num_len_input)]

for i in range(num_len_input):
    #Fill in every string on the Board
    bingo_boards_str[i] = [input[2 + x + (i * 6)] for x in range(5)]

bingo_boards = np.zeros((num_len_input, 5 ,5))

#Now we have to convert every string to a list of numbers
for i in range(num_len_input):
    for j in range(5):
        buffer = [int(s) for s in bingo_boards_str[i][j].split()]
        bingo_boards[i][j] = buffer

        print(i)




