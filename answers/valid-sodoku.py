def isValidSudoku(board: list[list[str]]) -> bool:
    d = {}
    for i in range(9):
        for j in range(9):
            if board[i][j] != '.':
                if (i, board[i][j]) in d or (board[i][j], j) in d or (i//3, j//3, board[i][j]) in d:
                    return False
                d[(i, board[i][j])] = 1
                d[(board[i][j], j)] = 1
                d[(i//3, j//3, board[i][j])] = 1
    return True