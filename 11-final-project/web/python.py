# run pip install chess
# pip install brython
# python -m pip install Django==6.0.4

from browser import document, html, svg

import django
import chess
import chess.svg

board = chess.Board()

print(str(board))

# piece = chess.svg.PIECES["n"]
# print(piece)

def selectPiece(event):
    print("Selected piece:", event.target.id)

# document["BoardSVG"].attach(xmlns="http://www.w3.org/2000/svg"), width=50, height=50 ,x=x, y=y)