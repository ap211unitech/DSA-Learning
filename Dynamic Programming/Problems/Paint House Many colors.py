
# Recommended - Go through "Paint House 3 colors.py" in this folder

# def solve(costs, n, k):

#     dp = [[-1 for i in range(k)] for j in range(n)]

#     for i in range(n):
#         for j in range(k):
#             if i == 0:
#                 dp[i][j] = costs[i][j]
#             else:
#                 dp[i][j] = costs[i][j]+min(dp[i-1][0:j]+dp[i-1][j+1::])  ### O(n^3)


#     # answer will be minimum of last row...
#     return min(dp[n-1])

def solve(costs, n, k):

    dp = [[-1 for i in range(k)] for j in range(n)]

    least_of_previous_array = float('inf')
    second_least_of_previous_array = float('inf')

    for i in range(n):
        new_least_of_previous_array = float('inf')
        new_second_least_of_previous_array = float('inf')

        for j in range(k):
            if i == 0:
                dp[i][j] = costs[i][j]
            else:
                dp[i][j] = costs[i][j]
                if least_of_previous_array == dp[i-1][j]:
                    dp[i][j] += second_least_of_previous_array
                else:
                    dp[i][j] += least_of_previous_array

            # Calculating least and second_least for current row
            if dp[i][j] <= new_least_of_previous_array:
                new_second_least_of_previous_array = new_least_of_previous_array
                new_least_of_previous_array = dp[i][j]
            elif dp[i][j] <= new_second_least_of_previous_array:
                new_second_least_of_previous_array = dp[i][j]

        # Updating least and second_least
        least_of_previous_array = new_least_of_previous_array
        second_least_of_previous_array = new_second_least_of_previous_array

    # answer will be minimum of last row...
    return min(dp[n-1])


n, k = map(int, input().split())
costs = []
for _ in range(n):
    costs.append(list(map(int, input().split())))

print(solve(costs, n, k))
