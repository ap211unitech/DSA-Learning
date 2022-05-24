
def LPS(s, t, n, m):
    dp = [[-1 for i in range(m+1)] for j in range(n+1)]

    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif s[i-1] == t[j-1]:
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[i][j]


s = input()
t = s[::-1]  # Reversing s
print(LPS(s, t, len(s), len(t)))
