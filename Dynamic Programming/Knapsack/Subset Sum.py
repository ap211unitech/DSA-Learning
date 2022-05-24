

def subsetSum(arr, n, k):
    dp = [[-1 for i in range(k+1)] for j in range(n+1)]

    for i in range(n+1):
        for j in range(k+1):
            if j == 0:
                dp[i][j] = True
            elif i == 0:
                dp[i][j] = False
            elif j >= arr[i-1]:
                dp[i][j] = (dp[i-1][j-arr[i-1]] or dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]

    return dp[i][j]


arr = list(map(int, input().split()))
givenSum = int(input())
print(subsetSum(arr, len(arr), givenSum))
