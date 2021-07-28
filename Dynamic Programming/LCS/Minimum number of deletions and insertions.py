def LCS(s, t, n, m):
    dp = [[-1 for i in range(m+1)] for j in range(n+1)]

    for i in range(n+1):
        for j in range(m+1):
            if i == 0:
                dp[i][j] = 0
            elif j == 0:
                dp[i][j] = 0
            elif s[i-1] == t[j-1]:
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # e.g heap and pea - LCS is ea (2) so , ans is (heap-ea)+(pea-ea)=2+1=3
    return n+m-2*dp[i][j]


s = input()
t = input()
print(LCS(s, t, len(s), len(t)))
