# In leetcode, this is given as Last stone weight (Beautiful Problem) https://leetcode.com/problems/last-stone-weight-ii/
def minimumSubsetDiffrence(arr, n):
    k = sum(arr)
    dp = [[-1 for i in range(k+1)] for j in range(n+1)]
    
    for i in range(n+1):
        for j in range(k+1):
            if j == 0:
                dp[i][j] = True
            elif i == 0:
                dp[i][j] = False
            elif j >= arr[i-1]:
                dp[i][j] = (dp[i-1][j-arr[i-1]] or dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]

    minimum = 10**9
    for i in range(k//2, -1, -1):
        if dp[n][i] == True:
            minimum = min(minimum, abs(k-2*i))
    return minimum


arr = list(map(int, input().split()))
print(minimumSubsetDiffrence(arr, len(arr)))
