
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        n = len(s)

        dp = [-1 for i in range(n+1)]
        dp[0] = 1  # Empty string has one subsequences

        latest = {}

        for i in range(1, n+1):

            dp[i] = 2*dp[i-1]  # subsequences till s[0:i-1]

            if s[i-1] in latest:
                dp[i] -= latest[s[i-1]]
            latest[s[i-1]] = dp[i-1]

        return (dp[n]-1) % (10**9+7)


s = input()
ob = Solution()
print(ob.distinctSubseqII(s))
