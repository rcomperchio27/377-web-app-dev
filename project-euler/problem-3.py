import math

def isprime(num):
    for i in range(2, round(math.sqrt(num))):
        if num % i == 0:
            return False
    return True


number = 600851475143
max = 0
i = 2

while i < math.sqrt(number):
    if number % i == 0 and isprime(i):
        max = i
    
    i += 1

print(max)