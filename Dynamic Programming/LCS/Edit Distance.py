def minDistance(s, t):
    dp = [[-1 for i in range(len(t)+1)] for j in range(len(s)+1)]

    for i in range(len(s)+1):
        for j in range(len(t)+1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1+min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])

    return dp[len(s)][len(t)]


s = input()
t = input()
print(minDistance(s, t))
