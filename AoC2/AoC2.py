import lib
import re

list = lib.input_as_string("input2.txt")

matches = [(dir, int(dist)) for (dir, dist) in re.findall(r'(\w+) (\d+)', list)]

h = 0
lateral = 0
aim = 0



for i in range(len(matches)):
    if matches[i][0] == "forward":
        lateral += matches[i][1]
        h += aim * matches[i][1]

    if matches[i][0] == "up":
        aim -= matches[i][1]

    if matches[i][0] == "down":
        aim += matches[i][1]

result = h * lateral

print(result)




