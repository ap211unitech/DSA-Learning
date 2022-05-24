def answer(arr, key):
    r = len(arr)
    c = len(arr[0])
    i = 0
    j = c-1

    while(i >= 0 and i < r and j >= 0 and j < c):
        if arr[i][j] == key:
            return True
        if arr[i][j] > key:
            j -= 1
        else:
            i += 1
    return False

