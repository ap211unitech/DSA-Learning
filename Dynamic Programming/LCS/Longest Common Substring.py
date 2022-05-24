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
            if res < dp[i][j]:
                row = i
                col = j
                res = max(dp[i][j], res)

    ans = ""
    while(dp[row][col] != 0):
        ans = s[row-1]+ans  # t[col-1]+ ans
        row -= 1
        col -= 1

    print('Length of longest common substring: ', res)
    print('Longest common substring: ', ans)


s = input()
t = input()
LCS(s, t, len(s), len(t))
