
def LIS(arr, n):

    dp = [1]*n

    for i in range(n):
        max_till_i = 0
        for j in range(0, i):
            if arr[j] < arr[i]:
                max_till_i = max(dp[j], max_till_i)

        dp[i] = max_till_i+1

    return max(dp)


arr = list(map(int, input().split()))
n = len(arr)
print(LIS(arr, n))
