
def LCS(s, t, n, m):
    dp = [[-1 for i in range(m+1)] for j in range(n+1)]

    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif s[i-1] == t[j-1]:
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    print('Length of shortest common supersequence: ', n+m-dp[i][j])

    # Printing LCS
    i = n
    j = m
    res = ""
    while(i > 0 and j > 0):
        if s[i-1] == t[j-1]:
            res = s[i-1] + res
            i -= 1
            j -= 1
        else:
            if dp[i-1][j] > dp[i][j-1]:
                res = s[i-1]+res
                i -= 1
            else:
                res = t[j-1]+res
                j -= 1
    while(i > 0):
        res = s[i-1]+res
        i -= 1
    while(j > 0):
        res = t[j-1]+res
        j -= 1
    print('Shortest common supersequence:', res)


s = input()
t = input()
LCS(s, t, len(s), len(t))
