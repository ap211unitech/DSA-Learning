
# Problem - https://www.pepcoding.com/resources/online-java-foundation/dynamic-programming-and-greedy/partition-into-subsets-official/ojquestion

# Hint - https://www.youtube.com/watch?v=IiAsqfjhZnY&list=PL-Jc9J83PIiG8fE6rj9F5a6uyQ5WPdqKy&index=29&t=490s


def answer(n, k):
    dp = [[-1 for i in range(k+1)] for j in range(n+1)]

    for i in range(n+1):
        for j in range(k+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif i < j:
                dp[i][j] = 0
            elif i == 1:
                dp[i][j] = 1
            elif i == j:
                dp[i][j] = 1
            else:
                dp[i][j] = j*dp[i-1][j]+dp[i-1][j-1]

    return dp[n][k]


n, k = map(int, input().split())
print(answer(n, k))
