file = open('day4-data.txt', 'r')
lines = file.readlines()

def part1():
    total = 0

    for line in lines:
        line = line.strip()
        split = line.split(',')
        first = split[0]
        second = split[1]
        firstpoint = [int(first.split('-')[0]), int(first.split('-')[1])]
        secondpoint = [int(second.split('-')[0]), int(second.split('-')[1])]
        if firstpoint[0] <= secondpoint[0] and firstpoint[1] >= secondpoint[1]:
            total += 1
        elif firstpoint[0] >= secondpoint[0] and firstpoint[1] <= secondpoint[1]:
            total += 1
    print(total)

def part2():
    total = 0

    for line in lines:
        line = line.strip()
        split = line.split(',')
        first = split[0]
        second = split[1]
        firstpoint = [int(first.split('-')[0]), int(first.split('-')[1])]
        secondpoint = [int(second.split('-')[0]), int(second.split('-')[1])]
        if firstpoint[0] >= secondpoint[0] and firstpoint[1] <= secondpoint[1]:
            total += 1
        elif firstpoint[0] >= secondpoint[0] and firstpoint[0] <= secondpoint[1]:
            total += 1
        elif firstpoint[0] <= secondpoint[0] and firstpoint[1] >= secondpoint[1]:
            total += 1
        elif firstpoint[1] >= secondpoint[0] and firstpoint[0] <= secondpoint[1]:
            total += 1
    print(total)

part2()