file = open('day5-data.txt', 'r')
lines = file.readlines()

import time

def part1():
    total = 0
    blank = True
    ranges = []
    nums = []

    # print('data:')
    for line in lines:
        line = line.strip()
        if line == '':
            blank = False
        if blank:
            ranges.append(line)
        elif line != '' and not blank:
            nums.append(int(line))
        # print(line)
    # print('--------')

    for i in range(len(nums)):
        for j in range(len(ranges)):
            min, max = ranges[j].split('-')
            if nums[i] >= int(min) and nums[i] <= int(max):
                total += 1
                # print(nums[i])
                break
    

    # print(ranges)
    # print(nums)
    print(total)

def simplify(ranges):
    poplist = []

    for j in range(len(ranges)):
        rmin, rmax = ranges[j].split('-')
        rmin = int(rmin)
        rmax = int(rmax)
        for i in range(len(ranges)):
            itemmin, itemmax = ranges[i].split('-')
            imin = int(itemmin)
            imax = int(itemmax)
            # print(imin, imax, rmin, rmax)
            # print('curent frange: ' + ranges[i])

            if rmin >= imin and rmax <= imax:
                pass
            elif rmin < imin and (rmax <= imax and rmax >= imin):
                ranges[i] = str(rmin) + '-' + str(imax)
                # print('replacemin')
            elif (rmin >= imin and rmin <= imax) and rmax > imax:
                ranges[i] = str(imin) + '-' + str(rmax)
                # print('replacemax')
            elif rmin <= imin and rmax >= imax:
                # print('replace')
                ranges[i] = str(rmin) + '-' + str(rmax)
            else:
                repeat = False

    newlist = list(set(ranges))
    return newlist
    

def addtorange(list, newrange):
    repeat = True
    rmin, rmax = newrange.split('-')
    rmin = int(rmin)
    rmax = int(rmax)
    for i in range(len(list)):
        itemmin, itemmax = list[i].split('-')
        imin = int(itemmin)
        imax = int(itemmax)
        print(imin, imax, rmin, rmax)
        print('curent frange: ' + list[i])

        if rmin >= imin and rmax <= imax:
            print('none')
        elif rmin < imin and (rmax <= imax and rmax >= imin):
            list[i] = str(rmin) + '-' + str(imax)
            print('replacemin')
        elif (rmin >= imin and rmin <= imax) and rmax > imax:
            list[i] = str(imin) + '-' + str(rmax)
            print('replacemax')
        elif rmin <= imin and rmax >= imax:
            print('replace')
            list[i] = str(rmin) + '-' + str(rmax)
        else:
            repeat = False

    if repeat == False:
        list.append(str(rmin) + '-' + str(rmax))
        print('add')
    simplify(list)

def part2():
    total = 0
    blank = True
    ranges = []
    ids = set()
    franges = []

    for line in lines:
        line = line.strip()
        if line == '':
            blank = False
        if blank:
            ranges.append(line)
    #     print(line)
    # print('--------')

    # for i in range(len(ranges)):
    #     rmin, rmax = ranges[i].split('-')
    #     rmin = int(rmin)
    #     rmax = int(rmax)
    #     for j in range(rmin, rmax + 1):
    #         ids.add(int(j))
    
    # total = len(ids)

    # franges.append(ranges[0])
    # for i in range(len(ranges)):
    #     repeat = True
    #     rmin, rmax = ranges[i].split('-')
    #     rmin = int(rmin)
    #     rmax = int(rmax)
    #     # print('----------------------')
    #     # print('current range:' + ranges[i])
    franges = ranges
    #     # find all the ranges that intersect and simply them
    franges = simplify(franges)


    time.sleep(0.1)   
    
    for i in range(len(franges)):
        rmin, rmax = franges[i].split('-')
        rmin = int(rmin)
        rmax = int(rmax)
        distance = rmax - rmin + 1
        total += distance

    print(franges)
    print(total)
        
part2()