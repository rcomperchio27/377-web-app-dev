from browser import document, html, svg, timer, window

# Get the full URL as a string
current_url = window.location.href

try: 
    usernum = str(current_url.split("/")[4])
except:
    usernum = "none"

print(usernum)

if usernum != "login":
    document["login-text"].html = "Login"
    document["Signup-button"].value = "Login"
    document["usernum"].html = usernum
    document["user_id-field"].value = usernum
        
    document["form-container"].hidden = True
    document["game-select-container"].hidden = False
    
else:
    document["login-text"].html = "Sign up"
    document["Signup-button"].value = "Sign up"

print(current_url)
document["User-name-text"].html = document["user_name" + str(usernum)].html

while True:
    users = document["Game-table"].html.split("<tr")[2:]
    for i in range(len(users)):
        row_id = users[i].split("id=")[1].split(">")[0][1:-1]
        id = users[i].split("id=")[2].split("hidden")[0][8:-2]

        if str(id) != str(document["usernum"].html) and str(id) != "":
            document["tr-row" + str(id)].hidden = True
    break


# document["form-container"].hidden = True
# document["game-select-container"].hidden = False