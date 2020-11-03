QUEENS = 10

def gradient_search(board):
    attacks = count_attacks(board)
    newpos = None
    queens = []
    for x in range(10):
        for y in range(10):
            if board[y][x] == 1:
                queens.append((y, x))
    for x in range(10):
        for y in range(10):
            if y != queens[x][0]:
                board[y][x] = 1
                board[queens[x][0]][queens[x][1]] = 0
                newattacks = count_attacks(board)
                if newattacks < attacks:
                    attacks = newattacks
                    newpos = (y, x)
                board[y][x] = 0
                board[queens[x][0]][queens[x][1]] = 1

    if newpos:
        board[newpos[0]][newpos[1]] = 1
        board[queens[newpos[1]][0]][queens[newpos[1]][1]] = 0
        gradient_search(board)
    else:
        return True if attacks == 0 else False

def count_attacks(board):
    attacks = 0
    row = [0 for i in range(10)]
    col = [0 for i in range(10)]
    diag1 = [0 for i in range(19)]
    diag2 = [0 for i in range(19)]

    for i in range(10):
        for j in range(10):
            if board[i][j] == 1:
                row[i] += 1
                col[j] += 1
                diag1[i+j] += 1
                diag2[2-i+j] += 1

    for i in range(10):
        attacks += row[i] * (row[i] - 1) / 2
        attacks += col[i] * (col[i] - 1) / 2
    for i in range(19):
        attacks += diag1[i] * (diag1[i] - 1) / 2
        attacks += diag2[i] * (diag2[i] - 1) / 2

    return attacks

