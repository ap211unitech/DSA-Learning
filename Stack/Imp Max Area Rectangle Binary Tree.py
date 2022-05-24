def MAH(arr, n):  # Code for Maximmum Area Histogram
    arr.append(0)  # For calculating last elemnt
    stack = []
    i = 0
    n = len(arr)
    max_area = 0

    while(i < n):
        while(stack and arr[stack[-1]] > arr[i]):
            h = arr[stack[-1]]
            stack.pop()
            if stack:
                max_area = max(max_area, h*(i-stack[-1]-1))
            else:
                max_area = max(max_area, h*i)

        stack.append(i)
        i += 1

    return max_area


def maximalRectangle(l):
    if len(l) == 0:
        return 0

    # Making them int
    for i in range(len(l)):
        for j in range(len(l[0])):
            l[i][j] = int(l[i][j])

    res = 0
    n = len(l[0])

    u = l[0]
    res = max(res, MAH(u, n))       # let l=[[0,1,1,0]
    #       ,[0,1,1,0],]
    # We will calculate MAH firstly for (0,1,1,0) then (0,2,2,0) and so on
    for i in range(1, len(l)):

        for j in range(n):
            if l[i][j] == 0:
                u[j] = 0
            else:
                u[j] += 1

        res = max(res, MAH(u, n))

    return res


rows = int(input())
columns = int(input())
arr = [[int(input()) for x in range(columns)] for y in range(rows)]

print(maximalRectangle(arr))
