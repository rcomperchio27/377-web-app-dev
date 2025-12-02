import time
file = open('day1-data.txt', 'r')
lines = file.readlines()

def part1():
    total = 0
    num = 50 

    for line in lines:
        print(line[0], line[1:])
        direction = line[0]
        amount = int(line[1:])

        if direction == 'L':
            num -= amount
        elif direction == 'R':
            num += amount
        num = num % 100
        print(num)
        if num == 0:
            total += 1

    print(total)


def part2():
    total = 0
    num = 50 
    count = 0
    for line in lines:
        line = line.strip()
        direction = line[0].upper()
        amount = int(line[1:])
        for i in range(amount):
            if direction == 'L':
                num = (num - 1) % 100
            else:
                num = (num + 1) % 100
            if num == 0:
                total += 1

    print(total)

part2()

# 6681 < x > 6739
# != 6698, 6708, 6703, 6712