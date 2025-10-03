file = open('day2-test.txt', 'r')
lines = file.readlines()

def part1():
    total = 0
    for line in lines:
        line = line.strip()
        line = line.split(' ')
        print(line)
        if line[1] == "X":
            total += 1
            if line[0] == "A":
                total += 3
            elif line[0] == "C":
                total += 6
        elif line[1] == "Y":
            total += 2
            if line[0] == "B":
                total += 3
            elif line[0] == "A":
                total += 6
        elif line[1] == "Z":
            total += 3
            if line[0] == "C":
                total += 3
            elif line[0] == "B":
                total += 6
        print(total)
    print("total score:" + str(total))


def part2():
    total = 0
    for line in lines:
        line = line.strip()
        line = line.split(' ')
        print(line)
        if line[1] == "X":
            total += 1
            if line[0] == "A":
                total += 2
            elif line[0] == "C":
                total += 1
        elif line[1] == "Y":
            total += 2
            if line[0] == "B":
                total += 2
            elif line[0] == "C":
                total += 4
        elif line[1] == "Z":
            total += 6
            if line[0] == "A":
                total += 2
            elif line[0] == "B":
                total += 3
            else:
                total += 1
        print(total)
    print("total score:" + str(total))

part2()