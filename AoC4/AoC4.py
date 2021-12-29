from lib import *
import numpy as np

def mark_board (board, key):
    for i in range(5):
        for j in range(5):
            if int(board[i][j]) == key:
                #WE use -1 as a marker for all the ticked of numbers
                board[i][j] = -1

    return board

def check_board (board):
    
    marker_vert = 0
    marker_horz = 0

    for i in range(5):
        for j in range(5):
            if int(board[i][j]) == -1:
                marker_vert = marker_vert + 1

            if int(board[j][i]) == -1:
                marker_horz = marker_horz + 1

        if marker_horz == 5 or marker_vert == 5:
            return True
        
        marker_vert = 0
        marker_horz = 0
    
    return False

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

#Now we need to iterate over the whole starting input to fill out the bingo bingo_board
marker = -1
last_number = -1
for i in range(100):
    key = num_order[i]
    
    for j in range(num_len_input):
        bingo_boards[j] = mark_board(bingo_boards[j], key)
    
    for j in range(num_len_input):
        if check_board(bingo_boards[j]) == True:
            marker = j #This is the board that finishes        
            break
    
    if marker != -1:
        last_number = key
        break
    
#Now we know the final board and the last number
sum = 0
for i in range(5):
    for j in range(5):
        if(bingo_boards[marker][i][j] != -1):
            sum += bingo_boards[marker][i][j]

print(int(sum * last_number))

