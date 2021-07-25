# def answer(arr):
#     n = len(arr)
#     l = 0
#     r = n-1

#     while(l <= r):
#         mid = l+(r-l)//2
#         if mid > 0 and mid < n-1:
#             if arr[mid] >= arr[mid-1] and arr[mid] >= arr[mid+1]:
#                 return mid
#             if arr[mid-1] > arr[mid]:
#                 r = mid-1
#             elif arr[mid+1] > arr[mid]:
#                 l = mid+1
#         elif mid == 0:
#             if arr[mid] > arr[mid+1]:
#                 return mid  # 0
#             else:
#                 return mid+1  # 1
#         elif mid == n-1:
#             if arr[mid] > arr[mid-1]:
#                 return mid # n-1
#             else:
#                 return mid-1 # n-2

def answer(arr):
    n = len(arr)
    l = 0
    r = n-1

    while(l <= r):
        mid = l+(r-l)//2

        if (mid == n-1 or arr[mid] >= arr[mid+1]) and (mid == 0 or arr[mid] >= arr[mid-1]):
            return arr[mid]

        elif mid > 0 and arr[mid] < arr[mid-1]:
            r = mid-1

        else:
            l = mid+1

    return -1


# Input
arr = list(map(int, input().split()))

print(answer(arr))
