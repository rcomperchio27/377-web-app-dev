import random
from sys import argv

SPECIALS = "!@#$%^&*()-=_+[][];:'<>,./?~`"

script, l, p = argv
print(script)
print(l)
print(p)

if (len(argv) == 3):
    length = int(argv[1])
else:
    length = int(input('How long should the password be?: '))
    includeNumber = input('Include a number? [Y/N] : ').upper()[0] == "Y"
    includeLower = input('Include a lowercase letter? [Y/N] : ').upper()[0] == "Y"
    includeUpper = input('Include an uppercase letter? [Y/N] : ').upper()[0] == "Y"
    includeSpecial = input('Include a special character? [Y/N]: ').upper()[0] == "Y"

password = []
if includeNumber:
    password.append(str(random.randint(0, 9)))
if includeLower:
    password.append(chr(ord("a") + random.randint(0, 25)))

if includeUpper:
    password.append(chr(ord("A") + random.randint(0, 25)))

if includeSpecial:
    password.append(SPECIALS[random.randint(0, len(SPECIALS) - 1)])


while len(password) < length:
    choice = random.randint(1, 4)

    if choice == 1 and includeNumber:
        password.append(str(random.randint(0, 9)))
    if choice == 2 and includeUpper:
        password.append(chr(ord("A") + random.randint(0, 25)))
    if choice == 3 and includeLower:
        password.append(chr(ord("a") + random.randint(0, 25)))
    if choice == 4 and includeSpecial:
        password.append(SPECIALS[random.randint(0, len(SPECIALS) - 1)])


random.shuffle(password)
print("".join(password))