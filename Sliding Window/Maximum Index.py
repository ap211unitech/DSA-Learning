def maxIndexDiff(arr, n):
    left = [arr[0]]

    for i in range(1, n):
        left.append(min(left[-1], arr[i]))

    right = [arr[-1]]

    for i in range(n-2, -1, -1):
        right.insert(0, max(right[0], arr[i]))

    i = 0
    j = 0
    res = 0

    while(i < n and j < n):
        if right[j] >= left[i]:
            res = max(res, j-i)
            j += 1
        else:
            i += 1

    return res


arr = list(map(int, input().split()))
n = len(arr)

print(maxIndexDiff(arr, n))  # May give TLE in python....but working on cpp correctly
