############################################# Recursion #############################################
# def answer(wt, val, w, n):
#     if n == 0 or w == 0:
#         return 0

#     if w >= wt[n-1]:
#         ans = max(answer(wt, val, w-wt[n-1], n-1) +
#                   val[n-1], answer(wt, val, w, n-1))
#     else:
#         ans = answer(wt, val, w, n-1)

#     return ans

############################################# Memoization #############################################
# def answer(wt, val, w, n, dp):
#     if n == 0 or w == 0:
#         return 0

#     if dp[n][w] != -1:
#         return dp[n][w]

#     if w >= wt[n-1]:
#         ans = max(answer(wt, val, w-wt[n-1], n-1, dp) +
#                   val[n-1], answer(wt, val, w, n-1, dp))
#     else:
#         ans = answer(wt, val, w, n-1, dp)

#     dp[n][w] = ans
#     return ans


############################################# Top Down #############################################
def answer(wt, val, w, n, dp):

    for i in range(n+1):
        for j in range(w+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif j >= wt[i-1]:
                dp[i][j] = max(dp[i-1][j-wt[i-1]]+val[i-1], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]

    return dp[i][j]


class Solution:

    # Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self, w, wt, val, n):
        dp = [[-1 for i in range(w+1)] for j in range(n+1)]
        return answer(wt, val, w, n, dp)
        # return answer(wt, val, w, n)


n = int(input())
w = int(input())
wt = list(map(int, input().split()))
val = list(map(int, input().split()))

ob = Solution()
print(ob.knapSack(w, wt, val, n))
