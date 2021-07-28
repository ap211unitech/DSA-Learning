def knapSack(n, w, val, wt):

    dp = [[-1 for i in range(w+1)] for j in range(n+1)]

    for i in range(n+1):
        for j in range(w+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif j >= wt[i-1]:
                dp[i][j] = max(val[i-1]+dp[i][j-wt[i-1]],  # Little change in this line
                               dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]

    return dp[i][j]


w = int(input())
val = list(map(int, input().split()))
wt = list(map(int, input().split()))
n = len(val)
print(knapSack(n, w, val, wt))
