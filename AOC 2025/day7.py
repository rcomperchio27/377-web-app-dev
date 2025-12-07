file = open('day7-data.txt', 'r')
lines = file.readlines()

import time

def part1():
    total = 1
    for i in range(1, len(lines)):
        lines[i] = list(lines[i].strip())
        line = lines[i]
        for j in range(len(line)):
            if lines[i][j] == '^' and lines[i - 1][j] == '|':
                if j != len(line):
                    lines[i][j + 1] = '|'
                if j != 0:
                    lines[i][j - 1] = '|'

                total += 2

            elif lines[i - 1][j] == 'S' or lines[i - 1][j] == '|':
                print(lines[i - 1][j])
                lines[i][j] = '|'
            print(line[j])
        print(lines[i])

    print("final")
    for line in lines:
        print(line)

    print(total)

def checkline(line, lines, i, j):
    if lines[i][j] == '^' and lines[i - 1][j] == '|':
        if j != len(line):
            lines[i][j + 1] = '|'
            lines[i][j] = '/'
            lines[i][j - 1] = '|'
        return True

    elif lines[i][j] == '/' and lines[i - 1][j] == '|':
        if j != 0:
                lines[i][j - 1] = '|'

        return True

    elif lines[i - 1][j] == 'S' or lines[i - 1][j] == '|':
        lines[i][j] = '|'


# def part2():
    total = 0
    final = [0, 0]
    secfinal = [0, 0]
    for i in range(1, len(lines)):
        lines[i] = list(lines[i].strip())
    for k in range(45):
        for i in range(1, len(lines)):
            line = lines[i]
            for j in range(len(line)):
                if lines[i][j] == '^' and lines[i - 1][j] == '|' and lines[i][j] != 'x':
                    if j != len(line):
                        lines[i][j + 1] = '|'
                        final = [i, j]
                        # lines[i][j] = '/'
                        # lines[i][j - 1] = '|'

                elif lines[i][j] == '/' and lines[i - 1][j] == '|' and lines[i][j] != 'x':
                    if j != 0:
                            lines[i][j - 1] = '|'
                            secfinal = final
                            final = [i, j]

                            lines[i][j] = 'x'

                elif (lines[i - 1][j] == 'S' or lines[i - 1][j] == '|') and lines[i][j] != 'x':
                    lines[i][j] = '|'

            for line in lines:
                print(line)
        time.sleep(0.5)

       
        if lines[final[0]][final[1]] == '^':
            lines[final[0]][final[1]] = '/'
            total += 1
        elif lines[final[0]][final[1]] == '/':
            lines[final[0]][final[1]] = 'x'
            lines[secfinal[0]][secfinal[1]] = '/'
            total += 1
        
        print(final)
        print(lines[final[0]][final[1]])
        print(total)

      



    print("final")
    for line in lines:
        print(line)

    print(total)

def getbelow(starti, startj, lines):
    value = 0
    print('value:' + str(value))
    for line in lines:
            print(line)    
    for i in range(starti, len(lines)):
        line = lines[i]
        for j in range(startj, len(line)):
            if lines[i][j] == '^' and lines[i - 1][j] == '|':
                print('hit')
                lines[i][j + 1] = '|'
                lines[i][j - 1] = '|'
                print("A")
                value += getbelow(i, j, lines)
                print('value:' + str(value))
            elif (lines[i - 1][j] == 'S' or lines[i - 1][j] == '|'):
                lines[i][j] = '|'

            if i == len(lines) and value == 0:
                print('aa')
                return 2
    print('value:' + str(value))

    return value

def part2():
    total = 0
    final = [0, 0]
    secfinal = [0, 0]
    for i in range(1, len(lines)):
        lines[i] = list(lines[i].strip())
    # for k in range(45):
    #     for i in range(1, len(lines)):
    #         line = lines[i]
    #         for j in range(len(line)):
    #             if lines[i][j] == '^' and lines[i - 1][j] == '|' and lines[i][j] != 'x':
    #                 if j != len(line):
    #                     lines[i][j + 1] = '|'
    #                     final = [i, j]
    #                     # lines[i][j] = '/'
    #                     # lines[i][j - 1] = '|'

    #             elif lines[i][j] == '/' and lines[i - 1][j] == '|' and lines[i][j] != 'x':
    #                 if j != 0:
    #                         lines[i][j - 1] = '|'
    #                         secfinal = final
    #                         final = [i, j]

    #                         lines[i][j] = 'x'

    #             elif (lines[i - 1][j] == 'S' or lines[i - 1][j] == '|') and lines[i][j] != 'x':
    #                 lines[i][j] = '|'

    #         for line in lines:
    #             print(line)
    #     time.sleep(0.5)

       
    #     if lines[final[0]][final[1]] == '^':
    #         lines[final[0]][final[1]] = '/'
    #         total += 1
    #     elif lines[final[0]][final[1]] == '/':
    #         lines[final[0]][final[1]] = 'x'
    #         lines[secfinal[0]][secfinal[1]] = '/'
    #         total += 1
        
        # print(final)
        # print(lines[final[0]][final[1]])
        # print(total)
    i = 14
    j = 1
    value = getbelow(i, j, lines)
    print(value)
    total += value
    print(total)

    print("final")
    for line in lines:
        print(line)

    print(total)
    
def splitterhit(lines, i, j, count):
    print(count)
    for line in lines:
        print(line)
    count += 1

    for i in range(1, len(lines)):
            line = lines[i]
            for j in range(len(line)):
                if lines[i][j] == '^' and lines[i - 1][j] == '|' and lines[i][j] != 'x':
                    if j != len(line) and j != 0:
                        lines[i][j + 1] = '|'
                        newtime = lines
                        print("A")
                        splitterhit(newtime, i, j, count)
                        lines[i][j - 1] = '|'
                        total += 1
                elif (lines[i - 1][j] == 'S' or lines[i - 1][j] == '|') and lines[i][j] != 'x':
                    lines[i][j] = '|'

def part3():
    total = 1
    timelines = []
    for i in range(len(lines)):
        lines[i] = list(lines[i].strip())
        print(lines[i])
    for i in range(1, len(lines)):
        line = lines[i]
        for j in range(len(line)):
            if lines[i][j] == '^' and lines[i - 1][j] == '|' and lines[i][j] != 'x':
                if j != len(line) and j != 0:
                    lines[i][j + 1] = '|'
                    newtime = lines
                    print('ap')
                    splitterhit(newtime, i, j, 0)
                    print('a')
                    lines[i][j - 1] = '|'
                    total += 1
            elif (lines[i - 1][j] == 'S' or lines[i - 1][j] == '|') and lines[i][j] != 'x':
                lines[i][j] = '|'

        # time.sleep(0.5)
    total += 1
    print(total)

    print("final")
    # for line in lines:
    #     print(line)

    # print(total)
    
def getvalue(lines, starti, startj, total):
    value = 0
    print(lines)
    print(total)

    print('value:' + str(value))
    for line in lines:
        print(line)    

    for i in range(starti, len(lines)):
        line = lines[i]
        for j in range(startj, len(line)):
            if lines[i][j] == '^' and lines[i - 1][j] == '|':
                lines[i][j + 1] = '|'
                lines[i][j - 1] = '|'
                value += getvalue(lines, i, j)
                print('value:' + str(value))
            elif (lines[i - 1][j] == 'S' or lines[i - 1][j] == '|'):
                lines[i][j] = '|'

            if i == len(lines) and value == 0:
                print('aa')
                return 2
    print('value:' + str(value))

    return value

# def part4():
#     total = 1
#     for i in range(len(lines)):
#         lines[i] = list(lines[i].strip())
#         print(lines[i])

#     for i in range(1, len(lines)):
#         line = lines[i]
#         for j in range(len(line)):
#             if lines[i][j] == '^' and lines[i - 1][j] == '|' and lines[i][j] != 'x':
#                 if j != len(line) and j != 0:
#                     lines[i][j + 1] = '|'
#                     print(total)

#                     total += getvalue(lines, i, j, total)
#                     print('a')
#                     lines[i][j - 1] = '|'
#             elif (lines[i - 1][j] == 'S' or lines[i - 1][j] == '|') and lines[i][j] != 'x':
#                 lines[i][j] = '|'

#         # time.sleep(0.5)
#     total += 1
#     print(total)

#     print("final")
#     # for line in lines:
#     #     print(line)

#     # print(total)
     
def part5():
    total = 0
    for i in range(len(lines)):
        lines[i] = list(lines[i].strip())

    for i in range(len(lines)):
        paths = []
        for j in range(len(lines[i])):
            if lines[i][j] == '^' and lines[i - 1][j] == '|':
                lines[i][j + 1] = '|'
                lines[i][j - 1] = '|'
                paths.append(j + 1)
                paths.append(j - 1)
            elif (lines[i - 1][j] == 'S' or lines[i - 1][j] == '|'):
                lines[i][j] = '|'
        total += len(paths)
        for line in lines:
            print(line)
        print(total)
        print(paths)
        print('----------')

def checkright(i, j, lines):
    print(lines[i])
    print(lines[i][j])
    # print("i:" + str(i))
    # for k in range(len(lines) - i, i, -1):
    #     current = lines[i][j - 1]
    #     print(current)
    #     if k == len(lines):
            # break
        # if current != '|':
        #     print(lines[i - k])
    return 1

def checkleft(i, j, lines):
    return 1

def part6():
    total = 0
    for i in range(len(lines)):
        lines[i] = list(lines[i].strip())

    for i in range(len(lines)):
        paths = []
        for j in range(len(lines[i])):
            if lines[i][j] == '^' and lines[i - 1][j] == '|':
                lines[i][j + 1] = '|'
                lines[i][j - 1] = '|'
                paths.append(j + 1)
                paths.append(j - 1)
            elif (lines[i - 1][j] == 'S' or lines[i - 1][j] == '|') and lines[i][j] == '.':
                lines[i][j] = '|'

    for l in range(len(lines)):
        i = len(lines) - l - 1
        for j in range(len(lines[i])):
            value = 0
            line = lines[i]
            if line[j] == '^' and lines[i - 1][j] == '|':
                for k in range(len(lines) - i):
                    if i + k == len(lines) - 1:
                        value += 1
                        break
                    point = lines[i + k][j + 1]
                    if point != '|' and point != '.' and point != '^':
                        value += int(point[0])
                        break
                for k in range(len(lines) - i):
                    if i + k == len(lines) - 1:
                        value += 1
                        break
                    point = lines[i + k][j - 1]
                    if point != '|' and point != '.' and point != '^':
                        value += int(point[0])
                        break
                line[j] = [value]
        # print(lines[i])

    for i in range(len(lines[2])):
        if lines[2][i] != '|' and lines[2][i] != '.' and lines[2][i] != '^':
           total = lines[2][i][0]
    # print('-------------------')
    # for line in lines:
    #     print(line)
        # print(total)
        # print(paths)
        # print('----------')
    print(total)
        
            
# 2996 < 

part6()

# .......S.......
# .......|.......
# ......|40.......
# ......|........
# .....|p.f......
# .....|.........
# ....|h.8.7.....
# ....|..........
# ...|a.7...6....
# ...|...........
# ..|5.5...2.4...
# ..|............
# .|4...4.....3..
# .|.............
# |2.2.2.2.2...2.
# |..............

# .......S.......
# .......1.......
# ......1^1......
# ......1.1......
# .....1^2^1.....
# .....1.2.1.....
# ....1^3^3^1....
# ....1.3.3.1....
# ...1^4^6.4^1...
# ...1.4.6.4.1...
# ..1^5^464^5^1..
# ..1.5.464.5.1..
# .1^154^a4.5^1.
# ...............
# .^.^.^.^.^...^.
# ...............