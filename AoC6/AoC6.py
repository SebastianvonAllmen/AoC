from lib import *
import re

input = input_as_string("input6.txt")

numbers = list(map(int, re.findall(r'(\d+)', input)))

REBIRTH_RATE = 7
DAYS = 256

# Simulate the amount of days
for i in range(1, DAYS):
    # here we deduct
    numbers = [members - 1 for members in numbers]
    # Step through every member of list
    for j in range(len(numbers)):
        # if days == 0 a new member is born
        if numbers[j] == 0:
            numbers[j] = REBIRTH_RATE
            numbers.append(REBIRTH_RATE+2)

print(len(numbers))
