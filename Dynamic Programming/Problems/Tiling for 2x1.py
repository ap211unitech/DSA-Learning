
# Make 2xN using 2x1 tiles

def solve(n):
    dp = [-1 for i in range(n+1)]

    dp[0] = 0
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n+1):
        dp[i] = dp[i-1]+dp[i-2]

    return dp[n]


n = int(input())
print(solve(n))
