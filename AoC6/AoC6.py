from lib import *
import re

REBIRTH_RATE = 7
fishage = [0] * 9

def solve(fishagetable, days):
    for _ in range(days):
        zero = fishagetable[0]
        fishagetable[0:8] = fishagetable[1:]
        fishagetable[REBIRTH_RATE-1] += zero
        fishagetable[REBIRTH_RATE+1] = zero
    return sum(fishagetable)

input = input_as_string("input6.txt")
numbers = list(map(int, re.findall(r'(\d+)', input)))

for number in numbers:
    fishage[number] += 1 

fishage2 = fishage.copy()

print(solve(fishage, 80))
print(solve(fishage2, 256))