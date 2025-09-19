file = open('day1-data.txt', 'r')
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


part2()
