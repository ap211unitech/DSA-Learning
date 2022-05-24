
def isSafe(chess, row, col):

    i = row-1
    j = col
    while(i >= 0):  # Checking Vertically up
        if chess[i][j] == "Q":
            return False
        i -= 1

    i = row-1
    j = col-1
    while(i >= 0 and j >= 0):  # Diagonal Right
        if chess[i][j] == "Q":
            return False
        i -= 1
        j -= 1

    i = row-1
    j = col+1
    while(i >= 0 and j < len(chess)):  # Diagonal Right
        if chess[i][j] == "Q":
            return False
        i -= 1
        j += 1

    return True


def answer(arr, row):
    if row == len(arr):
        print(arr)
        return

    for col in range(len(arr)):
        if isSafe(arr, row, col):
            arr[row][col] = "Q"
            answer(arr, row+1)
            arr[row][col] = "."


n = int(input())
arr = [['.' for i in range(n)] for j in range(n)]
answer(arr, 0)
