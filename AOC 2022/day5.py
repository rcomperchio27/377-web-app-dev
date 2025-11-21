file = open('day5-data.txt', 'r')
lines = file.readlines()
origin = 0
target = 0
amount = 0
# stacks = [
#     ['Z', 'N'],
#     ['M', 'C', 'D'],
#     ['P']
#     ] 
stacks = [
    ['Q', 'M', 'G', 'C', 'L'],
    ['R', 'D', 'L', 'C', 'T', 'F', 'H', 'G'],
    ['V', 'J', 'F', 'N', 'M', 'T', 'W', 'R'],
    ['J', 'F', 'D', 'V', 'Q', 'P'],
    ['N', 'F', 'M', 'S', 'L', 'B', 'T'],
    ['R', 'N', 'V', 'H', 'C', 'D', 'P'],
    ['H', 'C', 'T'],
    ['G', 'S', 'J', 'V', 'Z', 'N', 'H', 'P'],
    ['Z', 'F', 'H', 'G']
]

def part1():
    for line in lines:
        line = line.strip()
        words = line.split(" ")
        amount = int(words[1])
        origin = int(words[3]) - 1
        target = int(words[5]) - 1
        print(amount, origin, target)
        for i in range(amount):
            block = stacks[origin].pop()
            stacks[target].append(block)

    for i in range(len(stacks)):
        print(stacks[i][-1], end='')

def part2():
    for line in lines:
        line = line.strip()
        words = line.split(" ")
        amount = int(words[1])
        origin = int(words[3]) - 1
        target = int(words[5]) - 1

        stacks[target] = stacks[target] + stacks[origin][-amount:]
        del stacks[origin][-amount:]


    for i in range(len(stacks)):
        print(stacks[i][-1], end='')

part2()