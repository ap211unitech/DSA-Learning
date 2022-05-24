
# Prerequisite - Visit "/Tiling for 2x1.py"

def solve(n, m):
    # f(n,m) = f(n-1,m)+f(n-m,m)

    dp = [-1 for i in range(n+1)]
    mod = 10**9+7

    for i in range(n+1):
        if i < m:
            dp[i] = 1
        else:
            dp[i] = (dp[i-1] % mod+dp[i-m] % mod) % mod

    return dp[-1] % mod


n, m = map(int, input().split())
print(solve(n, m))
