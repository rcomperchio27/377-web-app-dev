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
    
    
else:
    document["login-text"].html = "Sign up"
    document["Signup-button"].value = "Sign up"

print(current_url)
document["User-name-text"].html = document["user_name" + str(usernum)].html

while True:
    users = document["Game-table"].html.split("<tr")[2:]
    for i in range(len(users)):
        print(users[i])
        id = users[i].split("id=")[1].split(">")[0][8:-1]
        print(id)
    print(len(users))
    print(users)
    break


document["form-container"].hidden = True
document["game-select-container"].hidden = False