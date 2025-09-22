file = open('day1-text.txt', 'r')
lines = file.readlines()
for line in lines:
    line = line.strip()
    print(line)
