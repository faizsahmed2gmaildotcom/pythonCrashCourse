TicTacToe = [
    ['X', 'O', 'X'],
    ['O', 'X', 'O'],
    ['X', 'O', 'O']
]

for a in range(len(TicTacToe)):
    print(TicTacToe[a])
print("'X' wins!")
print('\r')


chessBoard = [
    ['[]', '[]', '[]', '[]', '[]', '[]', '[]', '[]']
]
playingChessBoard = [
    ['{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}']
]

for b in range(len(chessBoard[0])):
    if (b == 0) or (b == 1) or (b == 6) or (b == 7):
        print(playingChessBoard[0][0] + playingChessBoard[0][1] + playingChessBoard[0][2] + playingChessBoard[0][3] + playingChessBoard[0][4] + playingChessBoard[0][5] + playingChessBoard[0][6] + playingChessBoard[0][7])
    else:
        print(chessBoard[0][0] + chessBoard[0][1] + chessBoard[0][2] + chessBoard[0][3] + chessBoard[0][4] + chessBoard[0][5] + chessBoard[0][6] + chessBoard[0][7])
