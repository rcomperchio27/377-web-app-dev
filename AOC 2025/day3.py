file = open('day3-test.txt', 'r')
lines = file.readlines()

def part1():
    total = 0

    for line in lines:
        line = line.strip()
        bank = [int(x) for x in line]
        index = -1
        max = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(12):
            for j in range(index + 1, len(bank) - 11 + i):

                if bank[j] > max[i]:
                    index = j
                    max[i] = bank[j]

        # for i in range(len(bank) - 2):
        #     if bank[i] > max:
        #         index = i
        #         max = bank[i]

        # for i in range(index + 1, len(bank) - 1):
        #     if bank[i] > max2:
        #         index2 = i
        #         max2 = bank[i]

        # for i in range(index2 + 1, len(bank)):
        #     if bank[i] > max3:
        #         max3 = bank[i]
        joltage = ''
        for i in range(11):
            joltage += str(max[i])
        print(joltage)
        total += int(joltage)
        print(max)
        print(bank)
    print(total)

part1()
  
# 17115202055671 < x > 