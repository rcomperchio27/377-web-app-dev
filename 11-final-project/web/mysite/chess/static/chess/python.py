# run pip install chess
# pip install brython
# python -m pip install Django==6.0.4
# python3 -m pip install svg.py

from browser import document, html, svg, timer, window

import chess

board = chess.Board()
abc = ["a", "b", "c", "d", "e", "f", "g", "h"]
strabc = "abcdefgh"
print(str(board))

print(board.legal_moves)
print(board)

def convertSqr(sqr):
    return (len(strabc.split(str(sqr[0]))[0]), 8 - int(sqr[len(list(sqr)) - 1]))

def move(sqr, origin, piece):
    if document["Player-turn"].html == "white":
        document["Player-turn"].html = "black"
    else:
        document["Player-turn"].html = "white"
    notation = chess.Board().san(chess.Move.from_uci(origin + sqr))
    try:
        board.push_san(notation)
        document["game_board_" + gamenum].html = str(board)
    except ValueError:
        return
    
    print(board)
    mov = convertSqr(sqr)
    document[piece].attrs["x"] = (int(mov[0]) * 80) + 12
    document[piece].attrs["y"] = (int(mov[1]) * 80) + 12

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
    print(str(piece))
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
    print(position)
    print(x, y)
    print(parts)
    print(event.target.id)

# Get the full URL as a string
current_url = window.location.href
print(current_url)

# ex:
# http://127.0.0.1:8000/chess/0/

gamenum = str(int(current_url.split("/")[4]) + 1)
document["gamenum"].html = gamenum

document["game_board_" + gamenum].html = str(board)

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