# run pip install chess
# pip install brython

from browser import document, html, svg

import chess
import chess.svg

board = chess.Board()

print(str(board))

# piece = chess.svg.piece(chess.Piece.from_symbol("R"))
piece = chess.svg.PIECES["R"]
print(piece)

document <= "<svg>" + str(piece) + "</svg>"