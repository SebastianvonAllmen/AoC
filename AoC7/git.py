import math

def main():
    with open("input7.txt", "r") as f:
        line = f.read()
        # print(part1(line))
        print(part2(line))

def median(lst):
    lst.sort()
    if len(lst) % 2 == 0:
        return (lst[len(lst) // 2] + lst[(len(lst) - 1) // 2]) / 2
    else:
        return lst[len(lst) // 2]

def part1(line):
    lineList = [int(item) for item in line.split(',')]
    median_value = int(median(lineList))
    return sum([abs(foo - median_value) for foo in lineList])

def part2(line):
    lineList = [int(item) for item in line.split(',')]
    mean0, mean1 = get_means(lineList)
    return min(
        sum(t(abs(item - mean0)) for item in lineList),
        sum(t(abs(item - mean1)) for item in lineList),
    )

def get_means(lineList):
    mean = sum(lineList) / len(lineList)
    return math.floor(mean), math.ceil(mean)

def t(n):
    return n * (n + 1) // 2

if __name__ == "__main__":
    main()
