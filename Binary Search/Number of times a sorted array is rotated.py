def findIndex(arr, l, r):  # actually we are finding index of minimum elemnt , that will be the number of times a array is rotated
    n = len(arr)
    while(l <= r):
        mid = l+((r-l)//2)

        prev = (mid-1+n) % n
        nex = (mid+1) % n

        if arr[mid] <= arr[prev] and arr[mid] <= arr[nex]:
            return mid
        elif arr[mid] < arr[0]:
            r = mid-1
        elif arr[-1] < arr[mid]:
            l = mid+1
        else:
            return 0

    return mid


arr = list(map(int, input().split()))

n = len(arr)

count = findIndex(arr, 0, n-1)
print(count)

# Similar questions
# 1) Find minimum in rotated sorted
# 2) Searching in rotated sorted