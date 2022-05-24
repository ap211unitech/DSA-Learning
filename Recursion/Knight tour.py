
def printChess(arr):
    for i in arr:
        for j in i:
            print(j, end=' ')
        print()
    print()


def knightTour(chess, move, row, col):
    # this is like visited array
    if row < 0 or col < 0 or row >= len(chess) or col >= len(chess[0]) or chess[row][col] > 0:
        return

    if move == len(chess)*len(chess[0]):
        chess[row][col] = move
        printChess(chess)
        chess[row][col] = 0
        return

    chess[row][col] = move
    knightTour(chess, move+1, row-2, col+1)
    knightTour(chess, move+1, row-1, col+2)
    knightTour(chess, move+1, row+1, col+2)
    knightTour(chess, move+1, row+2, col+1)
    knightTour(chess, move+1, row+2, col-1)
    knightTour(chess, move+1, row+1, col-2)
    knightTour(chess, move+1, row-1, col-2)
    knightTour(chess, move+1, row-2, col-1)
    chess[row][col] = 0


n = int(input())
row = int(input())
col = int(input())

chess = [[0 for i in range(n)] for j in range(n)]
knightTour(chess, 1, row, col)
