def left(arr, l, r, key):
    res = -1
    while(l <= r):
        mid = r+((l-r)//2)
        if arr[mid] == key:
            res = mid
            r = mid-1
        elif arr[mid] > key:
            r = mid-1
        else:
            l = mid+1
    return res


def right(arr, l, r, key):
    res = -1
    while(l <= r):
        mid = r+((l-r)//2)
        if arr[mid] == key:
            res = mid
            l = mid+1
        elif arr[mid] > key:
            r = mid-1
        else:
            l = mid+1
    return res


arr = list(map(int, input().split()))  # Sorted
key = int(input())
n = len(arr)
a = left(arr, 0, n-1, key)
b = right(arr, 0, n-1, key)
print(a, b) # for count we do b-a+1
