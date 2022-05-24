
# Visit - https://practice.geeksforgeeks.org/problems/stickler-theif-1587115621/1#
def FindMaxSum(arr, n):

    include = [0 for i in range(n)]
    exclude = [0 for i in range(n)]

    include[0] = arr[0]
    exclude[0] = 0

    for i in range(1, n):
        include[i] = exclude[i-1]+arr[i]
        exclude[i] = max(include[i-1], exclude[i-1])

    return max(include[n-1], exclude[n-1])


arr = list(map(int, input().split()))
n = len(arr)
print(FindMaxSum(arr, n))
