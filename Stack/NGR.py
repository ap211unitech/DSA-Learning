
# NGL, NSR and NSL based on this....

n = int(input())
arr = list(map(int, input().split()))

res = []

i = n-1
stack = []
res = []

while(i >= 0):
    while(stack and stack[-1] <= arr[i]):
        stack.pop()
    if stack:
        res.append(stack[-1])
        stack.append(arr[i])
    else:
        res.append(-1)
        stack.append(arr[i])
    i -= 1

res.reverse()
print(res)
