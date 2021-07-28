
def subsetSum(arr, n, k):
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

    if not dp[i][j]:
        print('No subsets can be formed..')
    else:
        printingSubsets(dp, arr)
    return dp[i][j]

# Printing subsets
def printingSubsets(dp, arr):
    i = len(dp)-1
    j = len(dp[0])-1
    set1 = []
    set2 = []
    while(j >= 0 and i > 0):
        if dp[i-1][j]:
            i -= 1
            set2.append(arr[i])

        elif dp[i-1][j-arr[i-1]]:
            i -= 1
            j -= arr[i]
            set1.append(arr[i])

    print(set1, set2)


class Solution:
    def equalPartition(self, n, arr):
        s = sum(arr)

        if s % 2 != 0:
            return 0

        s = s//2

        if (subsetSum(arr, n, s)):
            return 1
        return 0


arr = list(map(int, input().split()))
n = len(arr)
ob = Solution()
print(ob.equalPartition(n, arr))
