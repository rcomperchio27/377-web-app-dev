file = open('day1-test.txt', 'r')
lines = file.readlines()

def part1():
        
    max = 0
    max2 = 0
    max3 = 0
    current = 0

    for line in lines:
        line = line.strip()
        if line == '':
            if current > max:
                max = current
            current = 0
        else:
            current += int(line)

    print(max)

def part2():
    
    max = 0
    max2 = 0
    max3 = 0
    current = 0

    for line in lines:
        line = line.strip()
        if line == '':
            if current > max:
                temp = max2
                max2 = max
                max = current
                max3 = temp
            else:
                if current > max2:
                    max3 = max2
                    max2 = current
                else:
                    if current > max3:
                        max3 = current
            current = 0
        else:
            current += int(line)

    print(max + max2 + max3)

def part2b():

    total = 0
    totals = []
    for line in lines:
        line = line.strip()
        if line == '':
            totals.append(total)
            total = 0
        else:
            total += int(line)

    totals.append(total)
    totals.sort(reverse=True)
    print('part 2:' + sum(totals[0:3]))


part2b()