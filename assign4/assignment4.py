def nQueens(board, n,row, col):
    for i in range(0, n):
        # if utility function return true then queen can be placed else not

        place = utilityFunc(board, row, col)
        if place:
            board[row][col] = 1
            col += 1
            if col == 4:
                col = 0
                row += 1
                if row==4 :
                    return
        else:
            col += 1
            if col == 4:
                col = 0
                row += 1
                if row==4 :
                    return
            nQueens(board, n, row, col)



def utilityFunc(board, row1, col1):
    # if utility function return true then queen can be placed else not
    # queen can be placed if there is no queen in same row, column and diagonal

    can_be_placed = True

    if 0 < row1 < (n - 1) and 0 < col1 < (n - 1):

        if board[row1 - 1][col1 - 1] == 1:
            # left-top diagonal
            can_be_placed = False
        elif board[row1 + 1][col1 + 1] == 1:
            # right-top diagonal
            can_be_placed = False

    # check row
    curr_row = board[row1]
    for i in curr_row:
        if i == 1:
            can_be_placed = False

    # check col
    curr_col = []
    for k in range(0, n):
        curr_col.append(board[k][col1])

    for j in curr_col:
        if j == 1:
            can_be_placed = False

    # check diagonal
    # can_be_placed = check_diagonal(board, row1, col1, can_be_placed)

    return can_be_placed


def check_diagonal(board, row2, col2, can_be_placed1):
    if 0 < row2 < (n - 1) and 0 < col2 < (n - 1):

        if board[row2 - 1][col2 - 1] == 1:
            # left-top diagonal
            can_be_placed1 = False
        elif board[row2 + 1][col2 + 1] == 1:
            # right-top diagonal
            can_be_placed1 = False

    return can_be_placed1


n = int(input("Enter number of queens - "))
if n == 1:
    print("Trivial solution")
elif n == 2 or n == 3:
    print("No solution")
else:
    board = []
    for i in range(0, n):
        l = []
        for j in range(0, n):
            l.append(0)
        board.append(l)

    print(board)
    nQueens(board, n,0, 0)
    print(board)
