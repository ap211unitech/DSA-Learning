
# Given an integer N and a 2D array cost[][3], where cost[i][0], cost[i][1], and cost[i][2] is the cost of painting ith house with colors red, blue, and green respectively, the task is to find the minimum cost to paint all the houses such that no two adjacent houses have the same color.

# This is based on "Maximum Sum Non Adjacent Elements"


def solve(costs, n):

    dp = [[-1 for i in range(3)] for j in range(n)]

    for i in range(n):
        for j in range(3):
            if i == 0:
                dp[i][j] = costs[i][j]
            else:
                if j == 0:
                    dp[i][j] = costs[i][j]+min(dp[i-1][1], dp[i-1][2])
                elif j == 2:
                    dp[i][j] = costs[i][j]+min(dp[i-1][0], dp[i-1][1])
                else:
                    dp[i][j] = costs[i][j]+min(dp[i-1][0], dp[i-1][2])

    # dp == [14, 2, 11]
#           [13, 25, 7]
#           [21, 10, 23]

# answer will be minimum of last row...
    return min(dp[n-1])


costs = [[14, 2, 11],
         [11, 14, 5],
         [14, 3, 10]]
n = len(costs)

print(solve(costs, n))
