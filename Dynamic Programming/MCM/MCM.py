def answer(arr, i, j, dp):
    if i >= j:
        return 0

    minimum = 10**9

    if dp[i][j] != -1:
        return dp[i][j]

    for k in range(i, j):
        temp = answer(arr, i, k, dp)+answer(arr, k+1, j, dp) + \
            arr[i-1]*arr[k]*arr[j]
        minimum = min(temp, minimum)
        dp[i][j] = minimum

    return dp[i][j]


class Solution:
    def matrixMultiplication(self, n, arr):
        dp = [[-1 for i in range(n)] for j in range(n)]
        return answer(arr, 1, n-1, dp)


arr = list(map(int, input().split()))
n = len(arr)
ob = Solution()
print(ob.matrixMultiplication(n, arr))  # O(n^3)
