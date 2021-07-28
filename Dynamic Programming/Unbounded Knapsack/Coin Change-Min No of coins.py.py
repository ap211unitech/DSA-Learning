

def answer(coins, amount):
    INT_MAX = float('inf')
    n = len(coins)

    dp = [[-1 for i in range(amount+1)] for j in range(n+1)]

    for i in range(n+1):
        for j in range(amount+1):
            if i == 0:
                dp[i][j] = INT_MAX-1
            elif j == 0:
                dp[i][j] = 0
            elif i == 1:
                if j % coins[i-1] == 0:
                    dp[i][j] = j//coins[i-1]
                else:
                    dp[i][j] = INT_MAX-1
            elif j >= coins[i-1]:
                dp[i][j] = min(1+dp[i][j-coins[i-1]], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]

    if dp[i][j] == INT_MAX-1:
        return -1
    else:
        return dp[i][j]


coins = list(map(int, input().split()))
amount = int(input())
print(answer(coins, amount))
