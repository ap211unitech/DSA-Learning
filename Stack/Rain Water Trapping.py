def MaximumArrayLeft(arr):
    res = [arr[0]]

    for i in range(1, len(arr)):
        res.append(max(res[i-1], arr[i]))

    return res


def MaximumArrayRight(arr):
    res = [arr[-1]]

    for i in range(len(arr)-2, -1, -1):
        res.append(max(res[-1], arr[i]))
    res.reverse()
    return res


arr = list(map(int, input().split()))
n = len(arr)

MXL = MaximumArrayLeft(arr)
MXR = MaximumArrayRight(arr)
print(MXL)
print(MXR)
max_water_trapped = 0

for i in range(len(arr)):
    mx_left = MXL[i]
    mx_right = MXR[i]
    minimum = min(mx_left, mx_right)
    water_trapped = abs(minimum-arr[i])
    max_water_trapped += water_trapped

print(max_water_trapped)
