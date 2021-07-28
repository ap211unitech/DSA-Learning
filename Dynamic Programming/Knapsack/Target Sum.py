

def answer(arr, k):

    if k > sum(arr) or ((sum(arr)+k) % 2 != 0):
        return 0

    # s1-s2=k
    s1 = (k+sum(arr))//2

    n = len(arr)
    dp = [[-1 for i in range(s1+1)] for j in range(n+1)]

    for i in range(n+1):
        for j in range(s1+1):
            if i == 0 and j == 0:  # Fill tha table  correctly...
                dp[i][j] = 1
            elif i == 0:
                dp[i][j] = 0
            elif j >= arr[i-1]:
                dp[i][j] = dp[i-1][j-arr[i-1]]+dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]

    return dp[i][j]


arr = list(map(int, input().split()))
k = int(input())
