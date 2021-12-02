import lib
import re

class Uboot:
    def __init__(self):
        self.depth = 0
        self.lateral_position = 0
        self.aim = 0

    def change_position(self, direction, speed):
        if direction == "forward":
            self.lateral_position += speed
            self.depth += self.aim * speed

        if direction == "up":
            self.aim -= speed

        if direction == "down":
            self.aim += speed

list = lib.input_as_string("input2.txt")

matches = [(dir, int(dist)) for (dir, dist) in re.findall(r'(\w+) (\d+)', list)]

uboot = Uboot()

for i in range(len(matches)):
    uboot.change_position(matches[i][0], matches[i][1])
    
result = uboot.depth * uboot.lateral_position

print(result)






