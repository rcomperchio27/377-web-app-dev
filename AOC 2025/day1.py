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
        print(line[0], line[1:])
        direction = line[0].upper()
        amount = int(line[1:])
        prevnum = num
        if direction == 'L':
            num -= amount
        elif direction == 'R':
            num += amount
        if num == 0:
            total += 1
            print(num)
            print(total)
        while num >= 100:
            print(num)
            num -= 100
            total += 1
            print(total)
        while num < 0:
            print(num)
            num += 100
            total += 1
            print(total)

        count += 1
        # num = num % 100
        print(num)
        print(total)

        # if count == 30:
        #     time.sleep(180)



    print(total)

part2()

# 6681 < x > 6739
# != 6698, 6708