# run pip install chess
# pip install brython
# python -m pip install Django==6.0.4
# python3 -m pip install svg.py

from browser import document, html, svg, timer, window

import chess

abc = ["a", "b", "c", "d", "e", "f", "g", "h"]
strabc = "abcdefgh"


# Get the full URL as a string
current_url = window.location.href
print(current_url)

# ex:
# http://127.0.0.1:8000/chess/0/

gamenum = str(int(current_url.split("/")[4]))
document["form-action"].action = "/chess/" + gamenum + "/save/"
document["gamenum"].html = gamenum

fen = document["game_fen_" + gamenum].html
if not(fen):
    board = chess.Board()
else:
    board = chess.Board(fen)
document["game_board_" + gamenum].html = str(board)

def checkmate(player):
    document["GameOutcomeDisplay"].html = player + "'s by checkmate!"
    if player == "white":
        document["game-state"].html = "Win"
    else:
        document["game-state"].html = "Loss"
    print(player)

def resetPieces():
    for i in range(2):
        document["white-knight-" + str(i + 1)].attrs["x"] = -100
        document["white-knight-" + str(i + 1)].attrs["y"] = -100
    for i in range(2):
        document["black-knight-" + str(i + 1)].attrs["x"] = -100
        document["black-knight-" + str(i + 1)].attrs["y"] = -100
    for i in range(2):
        document["white-bishop-" + str(i + 1)].attrs["x"] = -100
        document["white-bishop-" + str(i + 1)].attrs["y"] = -100
    for i in range(2):
        document["black-bishop-" + str(i + 1)].attrs["x"] = -100
        document["black-bishop-" + str(i + 1)].attrs["y"] = -100
    for i in range(2):
        document["white-rook-" + str(i + 1)].attrs["x"] = -100
        document["white-rook-" + str(i + 1)].attrs["y"] = -100
    for i in range(2):
        document["black-rook-" + str(i + 1)].attrs["x"] = -100
        document["black-rook-" + str(i + 1)].attrs["y"] = -100
    for i in range(8):
        document["white-pawn-" + str(i + 1)].attrs["x"] = -100
        document["white-pawn-" + str(i + 1)].attrs["y"] = -100
    for i in range(8):
        document["black-pawn-" + str(i + 1)].attrs["x"] = -100
        document["black-pawn-" + str(i + 1)].attrs["y"] = -100
             
    document["white-king-1"].attrs["x"] = -100
    document["white-king-1"].attrs["y"] = -100
    document["black-king-1"].attrs["x"] = -100
    document["black-king-1"].attrs["y"] = -100
    document["white-queen-1"].attrs["x"] = -100
    document["white-queen-1"].attrs["y"] = -100
    document["black-queen-1"].attrs["x"] = -100
    document["black-queen-1"].attrs["y"] = -100



def movePiece(piece_id, position):
    document[piece_id].attrs["x"] = (int(position[0]) * 80) + 12
    document[piece_id].attrs["y"] = (int(position[1]) * 80) + 12

def displayBoard():
    resetPieces()
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
    layout = ""
    displaylayout = document["game_board_" + gamenum].html
    print(displaylayout)
    for i in range(len(displaylayout)):
        if displaylayout[i] != " " and displaylayout[i] != "\n":
            layout += (displaylayout[i])
            
    print(layout)

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

def convertSqr(sqr):
    return (len(strabc.split(str(sqr[0]))[0]), 8 - int(sqr[len(list(sqr)) - 1]))

def backbutton(event):
    pastboards = document["pastboards"].html.split(", ")
    print(pastboards)
    board = chess.Board(pastboards[len(pastboards) - 2])
    document["game_board_" + gamenum].html = board
    displayBoard()

def promotePawn(event):
    document["pawn-promotion-choice"].html = event.target.id.split('-')[0]
    document["promotion-menu"].attrs["visibility"] = "hidden"
    sqrloc = document["selectedSquare"].html.split(": ")[1]
    piece = document["selectedPiece"].html
    if piece == "":
        return
    piecetype = piece.split(" at ")[0]
    piecetype = piecetype.split(" Piece: ")[1]
    pieceloc = piece.split("at ")[1]

    move(sqrloc, pieceloc, piecetype)

def move(sqr, origin, piece):
    notation = board.san(chess.Move.from_uci(origin + sqr))
    print(notation)

    try:
        legalmoves = str(board.legal_moves).split("(")[1].split(")")[0].split(", ")
        print(legalmoves)
        move_is_legal = False
        promotion = False
        for i in range(len(legalmoves)):
            if len(list(legalmoves[i])) > 3:
                print(list(legalmoves[i])[1:3])
                
                if list(legalmoves[i])[1] + list(legalmoves[i])[2] == "8=" or list(legalmoves[i])[1] + list(legalmoves[i])[2] == "1=":
                    promotion = True
                    move_is_legal = True
        
        if promotion == False:
            for i in range(len(legalmoves)):
                if legalmoves[i] == notation:
                    move_is_legal = True


        if move_is_legal:
            print("----")
            print(notation)
        
            if list(notation)[1] == "8" or  list(notation)[1] == "1":
                promotePiece = document["pawn-promotion-choice"].html
                print(promotePiece)
                if promotePiece == "":
                    document["promotion-menu"].attrs["visibility"] = "visible"
                    return
                else:
                    document["promotion-menu"].attrs["visibility"] = "hidden"
                    if promotePiece == "knight":
                        board.push_san(board.san(chess.Move.from_uci(origin + sqr)) + 'N')
                    else:
                        board.push_san(board.san(chess.Move.from_uci(origin + sqr)) + list(promotePiece)[0].upper())
            else:
                board.push_san(notation)
                
            if board.is_checkmate(): 
                checkmate(document["Player-turn"].html)


            document["game_board_" + gamenum].html = str(board)
            document["fen"].html = board.fen()
            if document["Player-turn"].html == "white":
                document["Player-turn"].html = "black"
                document["PlayerTurnDisplay"].html = "Black's turn to move"
            else:
                document["Player-turn"].html = "white"
                document["PlayerTurnDisplay"].html = "White's turn to move"

            pastboards.append(str(board))
            document["pastboards"].html += str(board.fen()) + ", "

            # Checks for 3 move repetition
            repetition_count = 0
            for i in range(len(pastboards)):
                if pastboards[i] == str(board):
                    repetition_count += 1
            if repetition_count >= 3:
                document["game-state"].html = "Draw"

    except ValueError:
        return
    
    mov = convertSqr(sqr)
    document[piece].attrs["x"] = (int(mov[0]) * 80) + 12
    document[piece].attrs["y"] = (int(mov[1]) * 80) + 12
        
    document["fen"].html = board.fen()
    print(board)
    displayBoard()

def convertSquare(sqr):
    letter = sqr[0]
    num = sqr[1]
    return (len(strabc.split(str(letter))[0])) + ((int(num) - 1) * 8)


def selectSquare(event):
    document["selectedSquare"].html = "Selected Square: " + event.target.id
    sqrloc = event.target.id
    piece = document["selectedPiece"].html
    if piece == "":
        return
    piecetype = piece.split(" at ")[0]
    piecetype = piecetype.split(" Piece: ")[1]

    pieceloc = piece.split("at ")[1]
    move_str = pieceloc + sqrloc
    move(sqrloc, pieceloc, piecetype)

def selectPiece(event):
    piece = document[event.target.id]
    parts = str(piece).split(" ")

    for i in range(len(parts)):
        parts[i] = parts[i].split(">")[0]
        if len(parts[i].split("x=")) > 1:
            x = int(parts[i].split("x=")[1][1:-1])
        if len(parts[i].split("y=")) > 1:
            y = int(parts[i].split("y=")[1][1:-1])

    square = (x - 12) // 80, (y - 10) // 80
    position = str(abc[square[0]]) + str(8 - square[1])
    document["selectedPiece"].html = "Selected Piece: " + event.target.id + " at " + position
    # print(position)
    # print(x, y)
    # print(parts)
    # print(event.target.id)

def resetTimeControlButtons():
    document["3-minute"].attrs["fill"] = "#777777"

    for i in range(6):
        document[str((i + 1) * 5) + "-minute"].attrs["fill"] = "#777777"

    document["45-minute"].attrs["fill"] = "#777777"
    document["60-minute"].attrs["fill"] = "#777777"

def timeControlSelection(event):
    resetTimeControlButtons()
    if len(event.target.id.split("-")) == 3:
        textid = event.target.id
        id = textid.split("-")[0] + "-" + textid.split("-")[1]
        document[id].attrs["fill"] = "#555555"
    else:
        document[event.target.id].attrs["fill"] = "#555555"
    document["new-game-time-control"].html = event.target.id.split("-")[0]

def boardControlSelection(event):
    if len(event.target.id.split("-")) == 2:
        textid = event.target.id
        id = textid.split("-")[0]
        print(id)
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

def createGame(event):
    if document["new-game-time-control"].html == "":
        return
    missingPieces = {
        "Queen" : False,
        "Rooks" : False,
        "Bishops" : False,
        "Knights" : False
    }

    remove = document["new-game-board-control"].html.split("-")
    print(remove)
    defaultfen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    newfen = defaultfen.split(" ")[0]
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

    print(missingPieces)
        

    print(newfen)


    print(document["new-game-board-control"].html)
    print(document["new-game-time-control"].html)
    document["game-state"].html = "Pause"
    document["white-time-field"].value = str(int(document["new-game-time-control"].html) * 60)
    document["black-time-field"].value = str(int(document["new-game-time-control"].html) * 60)
    document["new-game-field"].value = "true"
    document["board-field"].value = newfen + " w - - 0 1"

    document["form-action"].submit()

def saveGame(event):
    document["form-action"].submit()
    # document[event.target.id].attrs["font-size"] = 40
    # document[event.target.id].html = "Save"
    
# uses fen to load games --------------------------------

fen = document["game_fen_" + gamenum].html

if not(fen):
    board = chess.Board()
else:
    board = chess.Board(fen)
    displayBoard()
    print(board)

document["fen"].html = board.fen()

# ---------------------------------------------------------------------
pastboards = [str(board)]

document["game_board_" + gamenum].html = str(board)
document["username"].html = document["game_user_" + gamenum].html


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

for i in range(8):
    for j in range(8):
        document[str(abc[i]) + str(j + 1)].bind("click", selectSquare)

if document["game_fen_" + gamenum].html.split(" ")[1] == "w":
    document["Player-turn"].html = "white"
    document["PlayerTurnDisplay"].html = "White's turn to move"
else:
    document["Player-turn"].html = "black"
    document["PlayerTurnDisplay"].html = "Black's turn to move"


document["3-minute-text"].bind("click", timeControlSelection)
document["3-minute"].bind("click", timeControlSelection)

for i in range(6):
    document[str((i + 1) * 5) + "-minute-text"].bind("click", timeControlSelection)
    document[str((i + 1) * 5) + "-minute"].bind("click", timeControlSelection)


document["45-minute-text"].bind("click", timeControlSelection)
document["45-minute"].bind("click", timeControlSelection)
document["60-minute-text"].bind("click", timeControlSelection)
document["60-minute"].bind("click", timeControlSelection)

document["no_queen"].bind("click", boardControlSelection)
document["no_queen-text"].bind("click", boardControlSelection)
document["no_rooks-text"].bind("click", boardControlSelection)
document["no_rooks"].bind("click", boardControlSelection)
document["no_bishops"].bind("click", boardControlSelection)
document["no_bishops-text"].bind("click", boardControlSelection)
document["no_knights-text"].bind("click", boardControlSelection)
document["no_knights"].bind("click", boardControlSelection)

document["create-game"].bind("click", createGame)

document["Save-btn"].bind("click", saveGame)
document["Save-btn-text"].bind("click", saveGame)

# document["Back-button"].bind("click", backbutton)
# document["pastboards"].html = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

document["queen-promote"].bind("click", promotePawn)
document["queen-promotion-background"].bind("click", promotePawn)
document["rook-promote"].bind("click", promotePawn)
document["rook-promotion-background"].bind("click", promotePawn)
document["bishop-promote"].bind("click", promotePawn)
document["bishop-promotion-background"].bind("click", promotePawn)
document["knight-promote"].bind("click", promotePawn)
document["knight-promotion-background"].bind("click", promotePawn)
