def is_solved(board):
    for i in range(3):
        if board[i][0] == 1 and board[i][1] == 1 and board[i][2] == 1:
            return 1
        elif board[i][0] == 2 and board[i][1] == 2 and board[i][2] == 2:
            return 2
        elif board[0][i] == 1 and board[1][i] == 1 and board[2][i] == 1:
            return 1
        elif board[0][i] == 2 and board[1][i] == 2 and board[2][i] == 2:
            return 2
        elif board[0][0] == 1 and board[1][1] == 1 and board[2][2] == 1:
            return 1
        elif board[0][0] == 2 and board[1][1] == 2 and board[2][2] == 2:
            return 2
    for row in range(3):
        for col in range(3):
            if board[row][col] == 0:
                return -1
    return 0


# not yet finished
board = [[0, 0, 1],
         [0, 1, 2],
         [2, 1, 0]]
print(is_solved(board), -1)

# winning row
board = [[1, 1, 1],
         [0, 2, 2],
         [0, 0, 0]]
print(is_solved(board), 1)

# winning column
board = [[2, 1, 2],
         [2, 1, 1],
         [1, 1, 2]]
print(is_solved(board), 1)

# draw
board = [[2, 1, 2],
         [2, 1, 1],
         [1, 2, 1]]
print(is_solved(board), 0)

board5 = [[2, 1, 1],
          [0, 1, 1],
          [2, 2, 2]]
print(is_solved(board5), 2)


# def isSolved(board):
#     for i in range(0, 3):
#         if board[i][0] == board[i][1] == board[i][2] != 0:
#             return board[i][0]
#         elif board[0][i] == board[1][i] == board[2][i] != 0:
#             return board[0][i]
#
#     if board[0][0] == board[1][1] == board[2][2] != 0:
#         return board[0][0]
#     elif board[0][2] == board[1][1] == board[2][0] != 0:
#         return board[0][0]
#
#     elif 0 not in board[0] and 0 not in board[1] and 0 not in board[2]:
#         return 0
#     else:
#         return -1
