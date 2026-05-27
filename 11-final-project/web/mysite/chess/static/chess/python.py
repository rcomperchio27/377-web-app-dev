# run pip install chess
# pip install brython
# python -m pip install Django==6.0.4

from browser import document, html, svg

# import django
import chess
import chess.svg
import time
from mysite.chess.views import GameIndexView
board = chess.Board()

print(str(board))

# piece = chess.svg.PIECES["n"]
# print(piece)

currentgame = games_list[0]
print(currentgame.game_time)

def selectPiece(event):
    print(event.target.id)
    print("Selected piece")

document["white-rook-1"].bind("click", selectPiece)
document["clock-text"].innerhtml = games_list[0].game_time

# document["BoardSVG"].attach(xmlns="http://www.w3.org/2000/svg"), width=50, height=50 ,x=x, y=y)