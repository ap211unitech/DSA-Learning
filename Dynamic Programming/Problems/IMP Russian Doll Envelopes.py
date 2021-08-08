
# Problem - https://leetcode.com/problems/russian-doll-envelopes/

# Approach - Sorting about width and LIS about height

class Solution:
    def maxEnvelopes(self, arr):
        n = len(arr)

        arr.sort(key=lambda x: x[0])

        dp = [0 for i in range(n)]
        dp[0] = 1

        for i in range(1, n):
            mx = 0
            for j in range(0, i):
                if arr[i][1] > arr[j][1] and arr[i][0] > arr[j][0]:
                    mx = max(dp[j], mx)

            dp[i] = mx+1

        return max(dp)
