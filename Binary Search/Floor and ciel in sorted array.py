def floor(arr, key):
    n = len(arr)
    l = 0
    r = n-1
    res = -1

    while(l <= r):
        mid = l+(r-l)//2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            res = max(mid, res)
            l = mid+1
        else:
            r = mid-1

    return res


def ciel(arr, key):
    n = len(arr)
    l = 0
    r = n-1
    res = 10**9

    while(l <= r):
        mid = l+(r-l)//2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            l = mid+1
        else:
            res = min(res, mid)
            r = mid-1

    if res == 10**9:
        return -1
    return res


arr = list(map(int, input().split()))
key = int(input())

n = len(arr)

print(floor(arr, key))
print(ciel(arr, key))
