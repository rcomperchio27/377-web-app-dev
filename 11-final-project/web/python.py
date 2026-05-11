# run pip install chess
# pip install brython
# python -m pip install Django==6.0.4

from browser import document, html, svg

# import django
import chess
import chess.svg

board = chess.Board()

print(str(board))

# piece = chess.svg.PIECES["n"]
# print(piece)

def selectPiece():
    print("Selected piece")

document["white-rook-1"].bind("click", selectPiece)

# document["BoardSVG"].attach(xmlns="http://www.w3.org/2000/svg"), width=50, height=50 ,x=x, y=y)