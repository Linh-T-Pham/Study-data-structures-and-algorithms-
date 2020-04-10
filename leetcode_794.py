""" A Tic-Tac-Toe board is given as a string array board. 
    Return True if and only if it is possible to reach this board position during 
    the course of a valid tic-tac-toe game.

    The board is a 3 x 3 array, and consists of characters " ", "X", and "O".  
    The " " character represents an empty square.
    Here are the rules of Tic-Tac-Toe:

    Players take turns placing characters into empty squares (" ").
    The first player always places "X" characters, while the second player always places "O" characters.
    "X" and "O" characters are always placed into empty squares, never filled ones.
    The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
    The game also ends if all squares are non-empty.
    No more moves can be played if the game is over.


    >>> ["o  ", "   ", "   "]
    false

    >>> ["xox", " x ", "   "]
    false

    >>> ["xxx", "   ", "ooo"]
    false

    >>> ["xox", "o  o", "xox"]
    true
"""

def validTicTacToe(board):
    o_count = 0
    x_count = 0
    
    for row in board:
        for char in row: 
            if char == "o": # count the number of O
                o_count += 1
            if char == "x": # count the number of X
                x_count += 1
        return o_count, x_count
        
def check_invalid_move(board, o_count, x_count):
    if o_count > x_count or x_count - 1 > o_count:
        return False # Check when the conditions false
    if 





if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. GO YOU!\n")



# class Solution(object):
#     def validTicTacToe(self, board):
#         """
#         :type board: List[str]
#         :rtype: bool
#         """
#         Xcount, Ocount = 0, 0
#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 if board[i][j] == 'x':
#                     Xcount += 1
#                 if board[i][j] == 'O':
#                     Ocount += 1
#         if Ocount > Xcount or Xcount-1>Ocount:
#                 return False
        
#         if Ocount >= 3:
#             flagX,flagO = False,False
#             for i in range(len(board)):
                # if board[i] == 'xxx' or [x[i] for x in board] == ['X','X','X']:
#                     flagX = True
#             if board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X':
#                 flagX = True
#             if board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
#                 flagX = True
#             if Xcount == Ocount and flagX:
#                 return False
#             for i in range(len(board)):
#                 if board[i] == 'OOO' or [x[i] for x in board] == ['O','O','O']:
#                     flagO = True
#                     if flagX:
#                         return False
#             if board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O':
#                     flagO = True
#                     if flagX:
#                         return False
#             if board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O':
#                     flagO = True
#                     if flagX:
#                         return False
#             if flagO:
#                 if Xcount - 1 == Ocount:
#                     return False
                    
#         return True
# 			```	