file = open('day6-data.txt', 'r')
lines = file.readlines()

import time
def removeblanks(list):
    remove = []
    for i in range(len(list)):
        if list[i] == '':
            remove.append(list[i])
    for i in range(len(remove)):
        list.remove(remove[i])
    return list
        
def part1():
    total = 0
    first = []
    second = []
    third = []

    for i in range(len(lines)):
        lines[i] = lines[i].strip()
        # print(lines[i])

    opperations = removeblanks(lines[4].split(' '))

    first = lines[0].split(' ')
    second = lines[1].split(' ')
    third = lines[2].split(' ')
    first = removeblanks(first)
    second = removeblanks(second)
    third = removeblanks(third)
    fourth = removeblanks(lines[3].split(' '))

    print(first)
    print(second)
    print(third)
    print(fourth)
    print(opperations)
    for i in range(len(opperations)):
        output = 0
        if opperations[i] == "+" or opperations[i] == "+ ":
            output = int(first[i]) + int(second[i]) + int(third[i]) + int(fourth[i])
        else:
            output = int(first[i]) * int(second[i]) * int(third[i]) * int(fourth[i])
        # print(output)
        total += output
    print(total)
    
def addblanks(str):
    # print('str:' + str)
    # if after == True:
    #     if len(str) == 1:
    #         str = str + '  '
    #     if len(str) == 2:
    #         str = str + ' '
    #     if len(str) == 3:
    #         str = str
    # else:
    #     if len(str) == 1:
    #         str =  '  '+ str 
    #     if len(str) == 2:
    #         str = ' ' + str 
    #     if len(str) == 3:
    #         str = str
    # if len(str) == 4:
    #     return '   ' + str
    # print('new str:' + str)
    return str
def makelist(given):
    
    addlist = []
    for i in range(len(given)):
       if i != len(given) - 1:
            # print(first[i])
            if given[i] == '' or given[i] == " ":
                addlist.append(i)
    # print(addlist)
    # print(first)
    # print('addlist stuff')
    for i in range(len(addlist)):
        index = addlist[0]
        given[index + 1] = ' ' + given[index + 1]
        # print(first[index + 1])

    given = removeblanks(given)
    return given

def findmax(ilist):
    max = len(ilist[0])
    for i in range(len(ilist)):
        if len(ilist[i]) > max:
            max = len(ilist[i])
    return max

def part2():
    total = 0
    text = ''
    for i in range(len(lines)):
        text += lines[i]
    # print(text)
    first, second, third, forth, opperations = text.split('\n')
    first = [first]
    second = [second]
    third = [third]
    forth = [forth]
    # print('-------------')

    opperations = removeblanks(lines[4].split(' '))
    count = 0
    for i in range(len(opperations) - 1):
        print('i:' + str(i))

        simplenums = [removeblanks(str(lines[0]).split(' '))[i], removeblanks(str(lines[1]).split(' '))[i], removeblanks(str(lines[2]).split(' '))[i], removeblanks(str(lines[3]).split(' '))[i]]
        inc = findmax(simplenums)
        # print("inc: " + str(inc))
        # print(first, second, third)
        # print('count: ' + str(count))
        fnum = first[0][count:inc + count]
        snum = second[0][count:inc + count]
        tnum = third[0][count:inc + count]
        xnum = forth[0][count:inc + count]
        # print('fnum...')
        # print(fnum)
        # print(snum)
        # print(tnum)
        # print(xnum)
        nums = [fnum, snum, tnum, xnum]
        count += inc + 1
        print('-----')

        firstnum = int(nums[0][0] + nums[1][0] + nums[2][0] + nums[3][0])
        print('f' + str(firstnum))
        if inc > 1: 
            secnum = int(nums[0][1] + nums[1][1] + nums[2][1] + nums[3][1])
            print('s' + str(secnum))

            if inc > 2: 
                thirdnum = int(nums[0][2] + nums[1][2] + nums[2][2] + nums[3][2])
                print('t' + str(thirdnum))

                if inc > 3: 
                    forthnum = int(nums[0][3] + nums[1][3] + nums[2][3] + nums[3][3])
                    print('4th' + str(forthnum))

                else:
                    if opperations[i] == "+" or opperations[i] == "+ ":
                        forthnum = int(0)
                    else:
                        forthnum = int(1)
            else:
                if opperations[i] == "+" or opperations[i] == "+ ":
                    thirdnum = int(0)
                    forthnum = int(0)
                else:
                    thirdnum = int(1)
                    forthnum = int(1)
        else:
            if opperations[i] == "+" or opperations[i] == "+ ":
                secnum = int(0)
                thirdnum = int(0)
                forthnum = int(0)
            else:
                secnum = int(1)
                thirdnum = int(1)
                forthnum = int(1)
        # print('1', '2', '3', '4')
        # print(firstnum, secnum, thirdnum, forthnum)
        output = 0
        if opperations[i] == "+" or opperations[i] == "+ ":
            output = int(firstnum) + int(secnum) + int(thirdnum) + int(forthnum)
        else:
            output = int(firstnum) * int(secnum) * int(thirdnum) * int(forthnum)
        # print(output, firstnum, secnum, thirdnum, forthnum)
        total += output
        # manually calced
        # total += 597324

    simplenums = [removeblanks(str(lines[0]).split(' '))[999], removeblanks(str(lines[1]).split(' '))[999], removeblanks(str(lines[2]).split(' '))[999], removeblanks(str(lines[3]).split(' '))[999]]
    inc = findmax(simplenums)
    # print("inc: " + str(inc))
    # print(first, second, third)
    # print('count: ' + str(count))
    fnum = first[0][count:inc + count]
    snum = second[0][count:inc + count]
    tnum = third[0][count:inc + count]
    xnum = forth[0][count:inc + count]
    # print('fnum...')
    # print(fnum)
    # print(snum)
    # print(tnum)
    # print(xnum)
    nums = [fnum, snum, tnum, xnum]
    count += inc + 1
    print('-----')

    inc = 2
    firstnum = int(nums[0][0] + nums[1][0] + nums[2][0] + nums[3][0])
    print('f' + str(firstnum))
    print(nums)
    if inc > 1: 
        secnum = int(nums[0][1] + nums[1][1] + nums[2][1] + nums[3][1])
        print('s' + str(secnum))

        if inc > 2: 
            thirdnum = int(nums[0][2] + nums[1][2] + nums[2][2] + nums[3][2])
            print('t' + str(thirdnum))

            if inc > 3: 
                forthnum = int(nums[0][3] + nums[1][3] + nums[2][3] + nums[3][3])
                print('4th' + str(forthnum))

            else:
                if opperations[999] == "+" or opperations[999] == "+ ":
                    forthnum = int(0)
                else:
                    forthnum = int(1)
        else:
            if opperations[999] == "+" or opperations[999] == "+ ":
                thirdnum = int(0)
                forthnum = int(0)
            else:
                thirdnum = int(1)
                forthnum = int(1)
    else:
        if opperations[999] == "+" or opperations[999] == "+ ":
            secnum = int(0)
            thirdnum = int(0)
            forthnum = int(0)
        else:
            secnum = int(1)
            thirdnum = int(1)
            forthnum = int(1)
    output = 0
    if opperations[999] == "+" or opperations[999] == "+ ":
        output = int(firstnum) + int(secnum) + int(thirdnum) + int(forthnum)
    else:
        output = int(firstnum) * int(secnum) * int(thirdnum) * int(forthnum)
    total += output
    
    print(total)
part2()

# 10951882148433 < > 10952478875109
