n = int(input())
arr = list(map(int, input().split()))


stack = []
res = []
i = 0
while(i < n):

    total_days_greater_than_today = 1  # itself
    while(len(stack) > 0 and stack[-1][0] <= arr[i]):
        total_days_greater_than_today += stack[-1][1]
        stack.pop()

    stack.append([arr[i], total_days_greater_than_today])
    res.append(stack[-1][1])
    i += 1

print(res)
