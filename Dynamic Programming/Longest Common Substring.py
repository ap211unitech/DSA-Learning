def LCS(s, t, n, m):

    dp = [[-1 for i in range(m+1)] for j in range(n+1)]
    res = -float('inf')

    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif s[i-1] == t[j-1]:
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j] = 0
            res = max(dp[i][j], res)

    print('Length of longest common substring: ', res)


s = input()
t = input()
LCS(s, t, len(s), len(t))
