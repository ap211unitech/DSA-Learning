n = int(input())
arr = list(map(int, input().split()))


if n == 1:
    print('Minimum Product: ', arr[0])
    print('Maximum Product: ', arr[0])
    exit()

inf = 10**9
zero, pos, neg = 0, 0, 0
minimum_positive = inf
maximum_negative = -inf
prod = 1

for i in range(n):
    if arr[i] == 0:
        zero += 1
        continue  # we will not include zero in our product
    elif arr[i] > 0:
        pos += 1
        minimum_positive = min(minimum_positive, arr[i])
    else:
        neg += 1
        maximum_negative = max(maximum_negative, arr[i])
    prod *= arr[i]

# Minimum Product
print('Minimum Product: ', end="")
if zero == n or (neg == 0 and zero > 0):
    print(0)

elif pos == n:
    print(minimum_positive)

elif neg % 2 == 0 and neg != 0:
    print(int(prod/maximum_negative))
else:
    print(prod)

# Maximum Product
print('Maximum Product: ', end="")
if zero == n:
    print(0)

elif neg % 2 == 1:
    if neg == 1 and zero > 0 and zero+neg == n:
        print(0)
    else:
        print(int(prod/maximum_negative))
else:
    print(prod)
