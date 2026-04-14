# run pip install chess
# pip install brython

from browser import document, html

import chess
import xml.etree.ElementTree as ET
import chess.svg

board = chess.Board()

print(board)
print(chess.svg.piece(chess.Piece.from_symbol("R")))

document = chess.Piece.from_symbol("R")