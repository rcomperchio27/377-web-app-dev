# run pip install chess

# from browser import document, html

# board = chess.Board()
# print(board)

from browser import document, html

# import chess
# import chess.svg
# board = chess.Board()
# print(board)

calc = html.TABLE()
calc <= html.TR(html.TH(html.DIV("0", id="result"), colspan=3) +
                html.TD("C", id="clear"))
lines = ["789/",
         "456*",
         "123-",
         "0.=+"]

calc <= (html.TR(html.TD(x) for x in line) for line in lines)

document <= calc