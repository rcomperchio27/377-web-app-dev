sum = 0
for i in range(99, 1, -1):
    for j in range(99, 1, -1):
        num = i * j
        num = list(str(num))
        firsthalf = str(num[:int(len(num) / 2)])
        sechalf = str(num[int(len(num) / 2):])
        print(firsthalf, sechalf)

        print(len(num))

print(sum)
