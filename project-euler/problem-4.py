import math

max = 0

def palindrome(max):
    for i in range(999, 1, -1):
        for j in range(i, 1, -1):
            if i * j > max:
                num = i * j
                num = list(str(num))
                firsthalf = num[:int(len(num) / 2)]
                sechalf = num[math.ceil(len(num) / 2):]
                sechalf.reverse()
                if str(firsthalf) == str(sechalf):
                    max = i * j
    return max

max = palindrome(0)

print(max)
