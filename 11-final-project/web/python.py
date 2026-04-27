# run pip install chess
# pip install brython
# python -m pip install Django==6.0.4

from browser import document, html, svg

import django
import chess
import chess.svg

board = chess.Board()

print(str(board))

piece = chess.svg.PIECES["R"]
print(piece)

document["BoardSVG"].attach(html.SVG(str(chess.svg.PIECES["R"]), xmlns="http://www.w3.org/2000/svg"), width=45, height=45)