
# One good approach is that find NSL and NSR for arr and take index array which will store NSR[i]-NSL[i]-1.
# Area , then can be calculated simply. In Some time, this can give TLE.

# def NearestSmallerToLeft(arr, n):
#     i = 0
#     stack = []
#     res = []

#     while(i < n):
#         while(stack and stack[-1][0] >= arr[i]):
#             stack.pop()
#         if stack:
#             res.append(stack[-1][1])  # Storing Index
#         else:
#             res.append(-1)
#         stack.append([arr[i], i])
#         i += 1

#     return res


# def NearestSmallerToRight(arr, n):
#     i = n-1
#     stack = []
#     res = []

#     while(i >= 0):
#         while(stack and stack[-1][0] >= arr[i]):
#             stack.pop()
#         if stack:
#             res.append(stack[-1][1])  # Storing Index
#         else:
#             res.append(n)
#         stack.append([arr[i], i])
#         i -= 1
#     res.reverse()
#     return res


n = int(input())
arr = list(map(int, input().split()))

# NSL = NearestSmallerToLeft(arr, n)
# NSR = NearestSmallerToRight(arr, n)

# max_area = float('-inf')

# for i in range(n):
#     max_area = max(max_area, arr[i]*(NSR[i]-NSL[i]-1))

# print(max_area)

arr.append(0)  # For calculating last elemnt
stack = []
i = 0
n = len(arr)
max_area = float('-inf')

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

print(max_area)
