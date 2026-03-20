import random

import tkinter as tk

file = open('diceware-wordlist-asc.txt', 'r')
lines = file.readlines()

root = tk.Tk()

def generate_password():
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
    strpassword = ''
    for i in range(len(password)):
        strpassword += password[i]
    messageVar.configure(text="Your password is " + strpassword)

tk.Label(root, text="Password").grid(row=0, column=0)

messageVar = tk.Message(root, text="")
messageVar.grid(row=4, column=0, columnspan=2)

entry1 = tk.Entry(root)
entry1.grid(row=1, column=1)

button = tk.Button(root, text="Generate New Password", width=25, command=generate_password)

button.grid(row=5, column=0, columnspan=1)

root.mainloop()