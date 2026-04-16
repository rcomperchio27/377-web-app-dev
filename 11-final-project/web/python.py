# run pip install chess
# pip install brython

from browser import document, html

import chess
import chess.svg

board = chess.Board()

print(str(board))

piece = chess.svg.piece(chess.Piece.from_symbol("R"))
print(piece)

document <= str(board)