import random

file = open('diceware.wordlist.asc.txt', 'r')
lines = file.readlines()

password = []
words = {}

for line in lines[2:7778]:
    dicenum = line.strip()[0:5]
    value = line.strip()[5:]

    words[str(dicenum.strip())] = str(value).strip()

for i in range(6):
    dice = str(random.randint(1, 6)) + str(random.randint(1, 6)) + str(random.randint(1, 6)) + str(random.randint(1, 6)) + str(random.randint(1, 6))
    password.append(words[str(dice)])

print(password)