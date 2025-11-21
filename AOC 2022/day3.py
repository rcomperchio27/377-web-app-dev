file = open('day3-test.txt', 'r')
lines = file.readlines()

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def part1():
    total = 0

    for line in lines:
    # // is opperator for division to be int instead of float
        firstHalf = line[:len(line) // 2]
        secondHalf = line[len(line) // 2:]
       
        print(line)
        for letter in firstHalf:
            if letter in secondHalf:
                total += int(alphabet.index(letter)) + 1

                print("Found Common letter: " + letter)
                break
    print(total)

r1 = "vJrwpWtwJgWrhcsFMMfFFhFp"
r2 = "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL"
r3 = "PmmdzqPrVvPwwTWBwg"


def part2():
    print()
    newlist = []
    # for i in range(int(len(lines) / 3)):
    #     newlist.append(lines[((i - 1) * 3)] + lines[((i - 1) * 3) + 1] + lines[((i - 1) * 3) + 2])
    # print(newlist)
    total = 0

    for line in lines:
    # // is opperator for division to be int instead of float
        firstHalf = line[:len(line) // 2]
        secondHalf = line[len(line) // 2:]
       
        print(line)
        for letter in firstHalf:
            if letter in secondHalf:
                total += int(alphabet.index(letter)) + 1
                newlist.append(letter)
                print("Found Common letter: " + letter)
                break
        
    print(total)
    print(newlist)

    # counter = 0
    # total = 0
    # for line in lines:
    #     counter += 1
    #     if counter % 3 == 1:
    #         string1 = lines[counter - 2]
    #         string2 = lines[counter - 1]
    #         string3 = lines[counter]

    #         print(lines[counter])
    #         for letter in string1:
    #         # // is opperator for division to be int instead of float
    #             for letter in string1:
    #                 if letter in string2 and letter in string3:
    #                     total += int(alphabet.index(letter)) + 1

    #                     print("Found Common letter: " + letter)
    #                     break
    # print(total)



part2()
