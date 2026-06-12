####################################################################################
# login.py
# 
# Main python file for the login.html page, contains functions for the login.html webpage and game table display
####################################################################################

# Imports libraries form browser 
from browser import document, window

# Get the full URL as a string
current_url = window.location.href

# Attempts to get the user's number from the URL
try: 
    usernum = str(current_url.split("/")[4])
except:
    usernum = "none"

# Checks if the user is currently logged in, if not the usernum would equal "login"
if usernum != "login":
    # Uses the users num to set the correct display for the login page
    document["login-text"].html = "Login"
    document["signup-button"].value = "Login"
    document["usernum"].html = usernum
    document["user_id-field"].value = usernum
    
    # User is already logged in so they find the games the user has stored
    document["form-container"].hidden = True
    document["game-select-container"].hidden = False
    
    # Sets the correct username from the table
    document["user-name-text"].html = document["user_name" + str(usernum)].html

else:
    # If the user isnt logged in displays sign up
    document["login-text"].html = "Sign up"
    document["signup-button"].value = "Sign up"

# Goes through the game table and only displays the games that are beign played by the correct user
while True:
    users = document["game-table"].html.split("<tr")[2:]
    for i in range(len(users)):
        row_id = users[i].split("id=")[1].split(">")[0][1:-1]
        id = users[i].split("id=")[2].split("hidden")[0][8:-2]

        if str(id) != str(document["usernum"].html) and str(id) != "":
            document["tr-row" + str(id)].hidden = True
    break