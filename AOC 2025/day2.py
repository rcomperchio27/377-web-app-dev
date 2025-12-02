file = open('day2-data.txt', 'r')
lines = file.readlines()

def part1():
    total = 0

    text = lines[0].split(',')
    for line in text:
        line = line.strip()
        start, end = (int(x) for x in line.split('-'))
        print(start, end)

        for i in range(start, end + 1):
            num = str(i)
            half = len(num) // 2
            first = num[:half]
            second = num[half:]
            if first == second:
                total += i
    print(total)

def part2():
    total = 0

    text = lines[0].split(',')
    for line in text:
        line = line.strip()
        start, end = (int(x) for x in line.split('-'))
        print(start, end)

        for n in range(start, end + 1):
            num = str(n)
            length = len(num)
            for l in range(1, length):
                if length % l == 0:
                    chunks = [num[i:i+l] for i in range(0, len(num), l)]
                    if len(set(chunks)) == 1:
                        print(num)
                        total += n
                        break
    print(total)


part2()
# 41653138746 < x >