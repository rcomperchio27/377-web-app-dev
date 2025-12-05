file = open('day4-data.txt', 'r')
lines = file.readlines()

grid = []
remove = []

def part1():
    total = 0

    for line in lines:
        row = [x for x in line.strip()]
        grid.append(row)

    for i in range(len(grid)):
        currentrow = grid[i]
        for j in range(len(grid[i])):
            proximity = 0
            current = currentrow[j]
            if current == '@':
                if j != 0:
                    if currentrow[j - 1] == '@':
                        proximity += 1

                if j != len(currentrow) - 1:
                    if currentrow[j + 1] == '@':
                        proximity += 1

                if i != 0:
                    if grid[i - 1][j] == '@':
                        proximity += 1
                        
                if i != len(grid) - 1:
                    if grid[i + 1][j] == '@':
                        proximity += 1

                if (i != 0) and (j != 0):
                    if grid[i - 1][j - 1] == '@':
                        proximity += 1

                if (i != len(grid[i]) - 1) and (j != 0):
                    if grid[i + 1][j - 1] == '@':
                        proximity += 1
                if (i != len(grid[i]) - 1) and (j != len(currentrow) - 1):
                    if grid[i + 1][j + 1] == '@':
                        proximity += 1
                if (i != 0) and (j != len(currentrow) - 1):
                    if grid[i - 1][j + 1] == '@':
                        proximity += 1

                if proximity < 4:
                    total += 1
                    remove.append([i, j])
                    # grid[i][j] = 'x'
            
                # for k in range(len(grid)):
                #     print(grid[k])
                # print(proximity)
                # print(total)

    print(total)
    # for i in range(len(grid)):
    #     print(grid[i])

def part2():
    total = 0
    
    for line in lines:
        row = [x for x in line.strip()]
        grid.append(row)
    
    while True:
        remove = []
        for i in range(len(grid)):
            currentrow = grid[i]
            for j in range(len(grid[i])):
                proximity = 0
                current = currentrow[j]
                if current == '@':
                    if j != 0:
                        if currentrow[j - 1] == '@':
                            proximity += 1

                    if j != len(currentrow) - 1:
                        if currentrow[j + 1] == '@':
                            proximity += 1

                    if i != 0:
                        if grid[i - 1][j] == '@':
                            proximity += 1
                            
                    if i != len(grid) - 1:
                        if grid[i + 1][j] == '@':
                            proximity += 1

                    if (i != 0) and (j != 0):
                        if grid[i - 1][j - 1] == '@':
                            proximity += 1

                    if (i != len(grid[i]) - 1) and (j != 0):
                        if grid[i + 1][j - 1] == '@':
                            proximity += 1
                    if (i != len(grid[i]) - 1) and (j != len(currentrow) - 1):
                        if grid[i + 1][j + 1] == '@':
                            proximity += 1
                    if (i != 0) and (j != len(currentrow) - 1):
                        if grid[i - 1][j + 1] == '@':
                            proximity += 1

                    if proximity < 4:
                        total += 1
                        remove.append([i, j])

        for a in range(len(remove)):
            index = remove[a]
            grid[index[0]][index[1]] = 'x'
        
        if len(remove) == 0:
            break

        # for k in range(len(grid)):
        #     print(grid[k])
        print(total)

    print(total)
    # for i in range(len(grid)):
    #     print(grid[i])

part2()