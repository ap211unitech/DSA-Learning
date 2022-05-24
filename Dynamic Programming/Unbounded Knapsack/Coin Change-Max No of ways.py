
def answer(coins, amount): # Recall Problem "Count subsets with given sum"
    n = len(coins)
    dp = [[-1 for i in range(amount+1)] for j in range(n+1)]

    for i in range(n+1):
        for j in range(amount+1):
            if j == 0:
                dp[i][j] = 1
            elif i == 0:
                dp[i][j] = 0
            elif j >= coins[i-1]:
                dp[i][j] = dp[i][j-coins[i-1]]+dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]

    return dp[i][j]


coins = list(map(int, input().split()))
amount = int(input())
print(answer(coins, amount))
