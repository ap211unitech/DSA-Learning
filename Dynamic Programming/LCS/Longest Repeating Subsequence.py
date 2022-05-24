

def answer(s, t, n, m):
    dp = [[-1 for i in range(m+1)] for j in range(n+1)]

    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            # Important step, Basically Index must be diffrent for occuring more than 1 time in same order...
            elif i != j and s[i-1] == t[j-1]:
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[i][j]


s = input()
print(answer(s, s, len(s), len(s)))
