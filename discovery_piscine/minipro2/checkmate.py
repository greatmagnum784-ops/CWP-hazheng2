def isvalidchess(list1):
    if not list1:
        return False
    clo = len(list1[0])
    i = 0
    while i < len(list1):
        if clo != len(list1[i]):
            return False
        i += 1
    if len(list1[0]) != len(list1):
        return False
    return True


def issometingblock(list1, rk, ck, r, c):
    while True:
        if rk > r:
            rk -= 1
        elif rk < r:
            rk += 1
        if ck > c:
            ck -= 1
        elif ck < c:
            ck += 1

        if rk == r and ck == c:
            break
        if list1[rk][ck] == 'Q' or list1[rk][ck] == 'R' or list1[rk][ck] == 'B' or list1[rk][ck] == 'P':
            return True
    return False


def isvalidking(list1):
    i = 0
    countking = 0
    whereking = 0
    while i < len(list1):
        j = 0
        while j < len(list1[i]):
            if list1[i][j] == 'K':
                whereking = (i * len(list1[i])) + j
                countking += 1
            j += 1
        i += 1
    if countking == 1:
        return whereking
    return -1


def istargetking(list1, c, r):
    i = 0
    while i < len(list1):
        j = 0
        while j < len(list1[i]):
            if list1[i][j] == 'Q' and (((i == r) or (j == c) or (abs(i - r) == abs(j - c))) and not issometingblock(list1, r, c, i, j)):
                return True
            elif list1[i][j] == 'R' and (((i == r) or (j == c)) and not issometingblock(list1, r, c, i, j)):
                return True
            elif list1[i][j] == 'B' and ((abs(i - r) == abs(j - c)) and not issometingblock(list1, r, c, i, j)):
                return True
            elif list1[i][j] == 'P' and ((i == r + 1) and (abs(j - c) == 1) and not issometingblock(list1, r, c, i, j)):
                return True
            j += 1
        i += 1
    return False

def checkmate(board):
    board_rows = board.split("\n")

    king = isvalidking(board_rows)
    if isvalidchess(board_rows) == False or king == -1:
        print("Error")
        return

    r = king // len(board_rows[0])
    c = king % len(board_rows[0])

    if istargetking(board_rows, c, r):
        print("Success")
    else:
        print("Fail")