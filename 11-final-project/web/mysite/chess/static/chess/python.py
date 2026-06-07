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

gamenum = str(int(current_url.split("/")[4]) + 1)
document["form-action"].action = "/chess/" + gamenum + "/save/"
document["gamenum"].html = gamenum
fen = document["game_fen_" + gamenum].html
if not(fen):
    board = chess.Board()
else:
    board = chess.Board(fen)
document["game_board_" + gamenum].html = str(board)

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

def move(sqr, origin, piece):
    notation = board.san(chess.Move.from_uci(origin + sqr))
    # print(board.is_capture(chess.Move(convertSquare(origin), convertSquare(sqr), None, None)))
    print(notation)

    try:
        legalmoves = str(board.legal_moves).split("(")[1].split(")")[0].split(", ")
        print(legalmoves)
        move_is_legal = False
        for i in range(len(legalmoves)):
            if legalmoves[i] == notation:
                move_is_legal = True
        
        if move_is_legal:
            board.push_san(notation)
            document["game_board_" + gamenum].html = str(board)
            document["fen"].html = board.fen()
            if document["Player-turn"].html == "white":
                document["Player-turn"].html = "black"
            else:
                document["Player-turn"].html = "white"

            pastboards.append(str(board))
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


# uses fen to load games --------------------------------

fen = document["game_fen_" + gamenum].html
if not(fen):
    board = chess.Board()
else:
    board = chess.Board(fen)
    displayBoard()
    print(board)

# ---------------------------------------------------------------------
pastboards = [str(board)]

document["game_board_" + gamenum].html = str(board)
document["username"].html = document["game_user_" + gamenum].html


for i in range(2):
    document["white-knight-" + str(i + 1)].bind("click", selectPiece)
for i in range(2):
    document["black-knight-" + str(i + 1)].bind("click", selectPiece)
for i in range(2):
    document["white-bishop-" + str(i + 1)].bind("click", selectPiece)
for i in range(2):
    document["black-bishop-" + str(i + 1)].bind("click", selectPiece)
for i in range(2):
    document["white-rook-" + str(i + 1)].bind("click", selectPiece)
for i in range(2):
    document["black-rook-" + str(i + 1)].bind("click", selectPiece)
for i in range(8):
    document["white-pawn-" + str(i + 1)].bind("click", selectPiece)
for i in range(8):
    document["black-pawn-" + str(i + 1)].bind("click", selectPiece)

document["white-king-1"].bind("click", selectPiece)
document["black-king-1"].bind("click", selectPiece)
document["white-queen-1"].bind("click", selectPiece)
document["black-queen-1"].bind("click", selectPiece)

for i in range(8):
    for j in range(8):
        document[str(abc[i]) + str(j + 1)].bind("click", selectSquare)

document["Player-turn"].html = "white"

