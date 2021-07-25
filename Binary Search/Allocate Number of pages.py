

def isValid(arr, n, k, mid):

    s = 0
    count = 1

    for i in range(n):
        s += arr[i]

        if s > mid:
            count += 1
            s = arr[i]

        if count > k:
            return False

    return True


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def books(self, arr, k):

        n = len(arr)

        if k > n:
            return -1

        start = max(arr)
        end = sum(arr)

        res = -1

        while(start <= end):
            mid = start+(end-start)//2

            if isValid(arr, n, k, mid):
                res = mid
                end = mid-1
            else:
                start = mid+1

        return res


arr = list(map(int, input().split()))
k = int(input())
ob = Solution()
print(ob.books(arr, k))
