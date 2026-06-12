####################################################################################
# pyhton.py
# 
# Main python file that contains functions for the index.html webpage and piece movements 
####################################################################################

# Commmands to run before using webiste

# run pip install chess
# pip install brython
# python -m pip install Django==6.0.4
# python3 -m pip install svg.py

# Imports important libraries from the browser and python-chess library
from browser import document, window
import chess

# Variables that contain the first letters of the alphabet
abc = ["a", "b", "c", "d", "e", "f", "g", "h"]
strabc = "abcdefgh"


# Gets the full URL as a string
current_url = window.location.href

# Breaks the URL up and gets the game_id number
gamenum = str(int(current_url.split("/")[4]))
document["form-action"].action = "/chess/" + gamenum + "/save/"
document["game-num"].html = gamenum

# Gets the game's fen and loads the board from it
fen = document["game_fen_" + gamenum].html
if not(fen):
    board = chess.Board()
else:
    board = chess.Board(fen)
document["game_board_" + gamenum].html = str(board)

# Runs when a give player gets checkmate and displays that information
def checkmate(player):
    document["game-outcome-display"].html = player + "'s by checkmate!"
    if player == "white":
        document["game-state"].html = "Win"
    else:
        document["game-state"].html = "Loss"

# Clears the pieces off the board
def resetPieces():
    for i in range(10):
        document["white-knight-" + str(i + 1)].attrs["x"] = -100
        document["white-knight-" + str(i + 1)].attrs["y"] = -100
    for i in range(10):
        document["black-knight-" + str(i + 1)].attrs["x"] = -100
        document["black-knight-" + str(i + 1)].attrs["y"] = -100
    for i in range(10):
        document["white-bishop-" + str(i + 1)].attrs["x"] = -100
        document["white-bishop-" + str(i + 1)].attrs["y"] = -100
    for i in range(10):
        document["black-bishop-" + str(i + 1)].attrs["x"] = -100
        document["black-bishop-" + str(i + 1)].attrs["y"] = -100
    for i in range(10):
        document["white-rook-" + str(i + 1)].attrs["x"] = -100
        document["white-rook-" + str(i + 1)].attrs["y"] = -100
    for i in range(10):
        document["black-rook-" + str(i + 1)].attrs["x"] = -100
        document["black-rook-" + str(i + 1)].attrs["y"] = -100
    for i in range(8):
        document["white-pawn-" + str(i + 1)].attrs["x"] = -100
        document["white-pawn-" + str(i + 1)].attrs["y"] = -100
    for i in range(8):
        document["black-pawn-" + str(i + 1)].attrs["x"] = -100
        document["black-pawn-" + str(i + 1)].attrs["y"] = -100
    for i in range(9):
        document["white-queen-" + str(i + 1)].attrs["x"] = -100
        document["white-queen-" + str(i + 1)].attrs["y"] = -100
    for i in range(9):
        document["black-queen-" + str(i + 1)].attrs["x"] = -100
        document["black-queen-" + str(i + 1)].attrs["y"] = -100
             
    document["white-king-1"].attrs["x"] = -100
    document["white-king-1"].attrs["y"] = -100
    document["black-king-1"].attrs["x"] = -100
    document["black-king-1"].attrs["y"] = -100

# Moves the piece on the SVG
def movePiece(piece_id, position):
    document[piece_id].attrs["x"] = (int(position[0]) * 80) + 12
    document[piece_id].attrs["y"] = (int(position[1]) * 80) + 12

# Displays the pieces on board
def displayBoard():
    resetPieces()
    # Keeps track of how many pieces are on the board
    tally = {
        "white-pawns" : 0,
        "white-rooks" : 0,
        "white-knights" : 0,
        "white-bishops" : 0,
        "white-queens" : 0,
        "white-kings" : 0,
        "black-pawns" : 0,
        "black-rooks" : 0,
        "black-knights" : 0,
        "black-bishops" : 0,
        "black-queens" : 0,
        "black-kings" : 0
    }

    # Formats the layout that is easy to display into a string
    layout = ""
    displaylayout = document["game_board_" + gamenum].html
    for i in range(len(displaylayout)):
        if displaylayout[i] != " " and displaylayout[i] != "\n":
            layout += (displaylayout[i])

    # Goes through the board and moves all the pieces
    for i in range(len(layout)):
        piece = layout[i]
        if piece != ".":
            position = [(i) % 8, (i) // 8]
            
            piece_id = ""
            if piece.isupper():
                piece_id += "white-"
            else:
                piece_id += "black-"
            if piece.lower() == "r":
                piece_id += "rook-"
            if piece.lower() == "n":
                piece_id += "knight-"
            if piece.lower() == "b":
                piece_id += "bishop-"
            if piece.lower() == "q":
                piece_id += "queen-"
            if piece.lower() == "k":
                piece_id += "king-"
            if piece.lower() == "p":
                piece_id += "pawn-"

            tally[piece_id[:-1] + 's'] += 1
            piece_id += str(tally[piece_id[:-1] + 's'])
            movePiece(piece_id, position)

# Converts a square in the notaion to a position in the SVG
def convertSqr(sqr):
    return (len(strabc.split(str(sqr[0]))[0]), 8 - int(sqr[len(list(sqr)) - 1]))

# Runs when a pawn in promoted, on click of a menu piece
def promotePawn(event):
    document["pawn-promotion-choice"].html = event.target.id.split('-')[0]
    document["promotion-menu"].attrs["visibility"] = "hidden"
    sqrloc = document["selected-square"].html.split(": ")[1]
    piece = document["selected-piece"].html
    if piece == "":
        return
    piecetype = piece.split(" at ")[0]
    piecetype = piecetype.split(" Piece: ")[1]
    pieceloc = piece.split("at ")[1]

    move(sqrloc, pieceloc, piecetype)

# Moves a given piece to a specific square checking first if the move is legal
def move(sqr, origin, piece):
    # Gets the move in terms of San notation
    notation = board.san(chess.Move.from_uci(origin + sqr))

    # Attempts move if it is legal
    try:
        legalmoves = str(board.legal_moves).split("(")[1].split(")")[0].split(", ")
        move_is_legal = False
        promotion = False
        # Checks if the move is a legal promotion
        for i in range(len(legalmoves)):
            if len(list(legalmoves[i])) > 3:
                
                if list(legalmoves[i])[1] + list(legalmoves[i])[2] == "8=" or list(legalmoves[i])[1] + list(legalmoves[i])[2] == "1=":
                    promotion = True
                    move_is_legal = True

        # Checks if the move is a legal move
        if promotion == False:
            for i in range(len(legalmoves)):
                if legalmoves[i] == notation:
                    move_is_legal = True

        # If the move is legal it will attempt the move
        if move_is_legal:
            # If move is a promotion it will show the menu if no piece selected or if one is selected promote to that piece
            if list(notation)[1] == "8" or  list(notation)[1] == "1":
                promotePiece = document["pawn-promotion-choice"].html
                if promotePiece == "":
                    document["promotion-menu"].attrs["visibility"] = "visible"
                    return
                else:
                    document["promotion-menu"].attrs["visibility"] = "hidden"
                    if promotePiece == "knight":
                        board.push_san(board.san(chess.Move.from_uci(origin + sqr)) + 'N')
                    else:
                        board.push_san(board.san(chess.Move.from_uci(origin + sqr)) + list(promotePiece)[0].upper())
            # If the move is not a promotion it will attempt the move
            else:
                board.push_san(notation)
                
            # Checks if the move was checkmate
            if board.is_checkmate(): 
                checkmate(document["player-turn"].html)

            # Updates the game board
            document["game_board_" + gamenum].html = str(board)
            document["fen"].html = board.fen()

            # Updates player move
            if document["player-turn"].html == "white":
                document["player-turn"].html = "black"
                document["player-turn-display"].html = "Black's turn to move"
            else:
                document["player-turn"].html = "white"
                document["player-turn-display"].html = "White's turn to move"

            pastboards.append(str(board))
            document["past-boards"].html += str(board.fen()) + ", "

            # Checks for 3 move repetition
            repetition_count = 0
            for i in range(len(pastboards)):
                if pastboards[i] == str(board):
                    repetition_count += 1
            if repetition_count >= 3:
                document["game-state"].html = "Draw"

    except ValueError:
        return
    
    # Moves the piece 
    mov = convertSqr(sqr)
    document[piece].attrs["x"] = (int(mov[0]) * 80) + 12
    document[piece].attrs["y"] = (int(mov[1]) * 80) + 12
        
    document["fen"].html = board.fen()

    # Displays the board
    displayBoard()

# Runs when a square is clicked
def selectSquare(event):
    # Gets the selected square
    document["selected-square"].html = "Selected Square: " + event.target.id
    sqrloc = event.target.id

    # Gets the selected piece if there is one
    piece = document["selected-piece"].html
    if piece == "":
        return
    piecetype = piece.split(" at ")[0]
    piecetype = piecetype.split(" Piece: ")[1]

    # Gets piece location and moves piece
    pieceloc = piece.split("at ")[1]
    move(sqrloc, pieceloc, piecetype)

# Runs when a piece is clicked on
def selectPiece(event):
    piece = document[event.target.id]
    parts = str(piece).split(" ")

    # Gets the pieces attributes like x and y
    for i in range(len(parts)):
        parts[i] = parts[i].split(">")[0]
        if len(parts[i].split("x=")) > 1:
            x = int(parts[i].split("x=")[1][1:-1])
        if len(parts[i].split("y=")) > 1:
            y = int(parts[i].split("y=")[1][1:-1])

    # Stores this information as the selected piece and its location
    square = (x - 12) // 80, (y - 10) // 80
    position = str(abc[square[0]]) + str(8 - square[1])
    document["selected-piece"].html = "Selected Piece: " + event.target.id + " at " + position

# Function to reset the colors of the time control buttons when a different one is clicked
def resetTimeControlButtons():
    document["3-minute"].attrs["fill"] = "#777777"

    for i in range(6):
        document[str((i + 1) * 5) + "-minute"].attrs["fill"] = "#777777"

    document["45-minute"].attrs["fill"] = "#777777"
    document["60-minute"].attrs["fill"] = "#777777"

# Sets a time control as a selection when its clicked
def timeControlSelection(event):
    # Resets all buttons
    resetTimeControlButtons()

    # Gets the id of the time control and sets it color
    if len(event.target.id.split("-")) == 3:
        textid = event.target.id
        id = textid.split("-")[0] + "-" + textid.split("-")[1]
        document[id].attrs["fill"] = "#555555"
    else:
        document[event.target.id].attrs["fill"] = "#555555"

    # Stores the selected time control
    document["new-game-time-control"].html = event.target.id.split("-")[0]

# Handels the board controls buttons when clicked it is selected/deselected changing its color and statis 
def boardControlSelection(event):
    if len(event.target.id.split("-")) == 2:
        textid = event.target.id
        id = textid.split("-")[0]
        if document[id].attrs["fill"] == "#555555":
            document[id].attrs["fill"] = "#777777"
            removelist = document["new-game-board-control"].html.split("-")
            removeset = set()
            for i in range(len(removelist)):
                if removelist[i] != "" and removelist[i] != str(id.split("_")[1]):
                    removeset.add(removelist[i])
            document["new-game-board-control"].html = ""
            for item in removeset:
                document["new-game-board-control"].html += str(item + '-')
        else:
            document[id].attrs["fill"] = "#555555"
            document["new-game-board-control"].html += id.split("_")[1] + "-"
    else:
        id = event.target.id
        if document[id].attrs["fill"] == "#555555":
            document[id].attrs["fill"] = "#777777"
            removelist = document["new-game-board-control"].html.split("-")
            removeset = set()
            for i in range(len(removelist)):
                if removelist[i] != "" and removelist[i] != str(id.split("_")[1]):
                    removeset.add(removelist[i])
            document["new-game-board-control"].html = ""
            for item in removeset:
                document["new-game-board-control"].html += str(item + '-')
        else:
            document[id].attrs["fill"] = "#555555"
            document["new-game-board-control"].html += id.split("_")[1] + '-'

# Handles the creation of the new game including information form the board controls and time controls buttons
def createGame(event):
    # If no time control selected returns
    if document["new-game-time-control"].html == "":
        return
    
    missingPieces = {
        "Queen" : False,
        "Rooks" : False,
        "Bishops" : False,
        "Knights" : False
    }
    # Gets the string of pieces to remove and the fen for a default game
    remove = document["new-game-board-control"].html.split("-")
    defaultfen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    newfen = defaultfen.split(" ")[0]

    # Removes the pieces in the string
    for i in range(len(remove)):
        if remove[i] == "queen":
                missingPieces["Queen"] = True
        if remove[i] == "rooks":
                missingPieces["Rooks"] = True
        if remove[i] == "bishops":
                missingPieces["Bishops"] = True
        if remove[i] == "knights":
                missingPieces["Knights"] = True

    if missingPieces["Rooks"] == True:
        newfen = "1" + newfen[1:]
        newfen = newfen.split("r")[0] + "1" + newfen.split("r")[1]
        newfen = newfen[:-1]
        newfen = newfen.split("R")[0] + "1" + newfen.split("R")[1] + "1"
    
    if missingPieces["Knights"] == True:
        if newfen[0] == "1":
            newfen = "2" + newfen[2:-2] + "2"
            newfen = newfen.split("n1")[0] + "2" + newfen.split("n1")[1]
            newfen = newfen.split("1N")[0] + "2" + newfen.split("1N")[1]
        else:
            newfen = newfen.split("n")[0] + "1" + newfen.split("n")[1] + "1" + newfen.split("n")[2]
            newfen = newfen.split("N")[0] + "1" + newfen.split("N")[1] + "1" + newfen.split("N")[2]
    if missingPieces["Bishops"] == True:
        if missingPieces["Knights"] == True:
            if missingPieces["Rooks"] == True:
                newfen = "3" + newfen[2:-2] + "3"
                newfen = newfen.split("b2")[0] + "3" + newfen.split("b2")[1]
                newfen = newfen.split("2B")[0] + "3" + newfen.split("2B")[1]
            else:
                newfen = "r2qk2r/pppppppp/8/8/8/8/PPPPPPPP/R2QK2R"

        else:
            newfen = newfen.split("b")[0] + "1" + newfen.split("b")[1] + "1" + newfen.split("b")[2]
            newfen = newfen.split("B")[0] + "1" + newfen.split("B")[1] + "1" + newfen.split("B")[2]
    
    if missingPieces["Queen"] == True and missingPieces["Bishops"] == False:
        newfen = newfen.split("q")[0] + "1" + newfen.split("q")[1]
        newfen = newfen.split("Q")[0] + "1" + newfen.split("Q")[1]

    
    if missingPieces["Queen"] == True and missingPieces["Bishops"] == True and missingPieces["Knights"] == False and missingPieces["Rooks"] == True:
        newfen = "2n1kn2/pppppppp/8/8/8/8/PPPPPPPP/2N1KN2"
    if missingPieces["Queen"] == True and missingPieces["Bishops"] == True and missingPieces["Knights"] == False and missingPieces["Rooks"] == False:
        newfen = "r1n1kn1r/pppppppp/8/8/8/8/PPPPPPPP/R1N1KN1R"
    if missingPieces["Queen"] == True and missingPieces["Bishops"] == True and missingPieces["Knights"] == True and missingPieces["Rooks"] == False:
        newfen = "r3k2r/pppppppp/8/8/8/8/PPPPPPPP/R3K2R"
    if missingPieces["Queen"] == True and missingPieces["Bishops"] == True and missingPieces["Knights"] == True and missingPieces["Rooks"] == True:
            newfen = "4k3/pppppppp/8/8/8/8/PPPPPPPP/4K3"    

    # Changes game state to stop updating the fields and input the selceted values
    document["game-state"].html = "Pause"
    document["white-time-field"].value = str(int(document["new-game-time-control"].html) * 60)
    document["black-time-field"].value = str(int(document["new-game-time-control"].html) * 60)
    document["new-game-field"].value = "true"
    document["board-field"].value = newfen + " w - - 0 1"

    # Saves the new game as a new game
    document["form-action"].submit()

# Saves game
def saveGame(event):
    document["form-action"].submit()
    
# uses fen to load games --------------------------------

fen = document["game_fen_" + gamenum].html

if not(fen):
    board = chess.Board()
else:
    board = chess.Board(fen)
    displayBoard()

document["fen"].html = board.fen()

# ---------------------------------------------------------------------
# Sets board and username
pastboards = [str(board)]
document["game_board_" + gamenum].html = str(board)
document["username"].html = document["game_user_" + gamenum].html

# Binds function to pieces
for i in range(10):
    document["white-knight-" + str(i + 1)].bind("click", selectPiece)
for i in range(10):
    document["black-knight-" + str(i + 1)].bind("click", selectPiece)
for i in range(10):
    document["white-bishop-" + str(i + 1)].bind("click", selectPiece)
for i in range(10):
    document["black-bishop-" + str(i + 1)].bind("click", selectPiece)
for i in range(10):
    document["white-rook-" + str(i + 1)].bind("click", selectPiece)
for i in range(10):
    document["black-rook-" + str(i + 1)].bind("click", selectPiece)
for i in range(8):
    document["white-pawn-" + str(i + 1)].bind("click", selectPiece)
for i in range(8):
    document["black-pawn-" + str(i + 1)].bind("click", selectPiece)
for i in range(9):
    document["white-queen-" + str(i + 1)].bind("click", selectPiece)
for i in range(9):
    document["black-queen-" + str(i + 1)].bind("click", selectPiece)

document["white-king-1"].bind("click", selectPiece)
document["black-king-1"].bind("click", selectPiece)

# Binds function to squares
for i in range(8):
    for j in range(8):
        document[str(abc[i]) + str(j + 1)].bind("click", selectSquare)

# Gets players game turn from the fen
if document["game_fen_" + gamenum].html.split(" ")[1] == "w":
    document["player-turn"].html = "white"
    document["player-turn-display"].html = "White's turn to move"
else:
    document["player-turn"].html = "black"
    document["player-turn-display"].html = "Black's turn to move"

# Binds time control buttons with the selection function
document["3-minute-text"].bind("click", timeControlSelection)
document["3-minute"].bind("click", timeControlSelection)

for i in range(6):
    document[str((i + 1) * 5) + "-minute-text"].bind("click", timeControlSelection)
    document[str((i + 1) * 5) + "-minute"].bind("click", timeControlSelection)

document["45-minute-text"].bind("click", timeControlSelection)
document["45-minute"].bind("click", timeControlSelection)
document["60-minute-text"].bind("click", timeControlSelection)
document["60-minute"].bind("click", timeControlSelection)

# Binds the remove pieces function with board control selection function
document["no_queen"].bind("click", boardControlSelection)
document["no_queen-text"].bind("click", boardControlSelection)
document["no_rooks-text"].bind("click", boardControlSelection)
document["no_rooks"].bind("click", boardControlSelection)
document["no_bishops"].bind("click", boardControlSelection)
document["no_bishops-text"].bind("click", boardControlSelection)
document["no_knights-text"].bind("click", boardControlSelection)
document["no_knights"].bind("click", boardControlSelection)

# Create game and save game binds
document["create-game"].bind("click", createGame)
document["save-btn"].bind("click", saveGame)
document["save-btn-text"].bind("click", saveGame)

# Promotion functions binded to promotion menu
document["queen-promote"].bind("click", promotePawn)
document["queen-promotion-background"].bind("click", promotePawn)
document["rook-promote"].bind("click", promotePawn)
document["rook-promotion-background"].bind("click", promotePawn)
document["bishop-promote"].bind("click", promotePawn)
document["bishop-promotion-background"].bind("click", promotePawn)
document["knight-promote"].bind("click", promotePawn)
document["knight-promotion-background"].bind("click", promotePawn)
