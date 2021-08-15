
# PROBLEM - https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/

def numSubseq(arr, k):
    arr.sort()
    n = len(arr)

    v = [1]
    for i in range(1, n):
        v.append((v[i-1]*2) % (10**9+7))

    i = 0
    j = n-1
    res = 0

    while(i <= j):
        if arr[i]+arr[j] <= k:
            res += v[j-i] % (10**9+7)
            i += 1
        else:
            j -= 1

    return res % (10**9+7)


arr = list(map(int, input().split()))
k = int(input())
print(numSubseq(arr, k))
