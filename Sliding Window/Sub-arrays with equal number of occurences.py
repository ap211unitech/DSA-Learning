
# PROBLEM - https://practice.geeksforgeeks.org/problems/sub-arrays-with-equal-number-of-occurences3901/1#

class Solution:
    def sameOccurrence(self, arr, n, x, y):

        if x == y:
            return n*(n+1)//2

        for i in range(n):
            if arr[i] == x:
                arr[i] = -1
            elif arr[i] == y:
                arr[i] = 1
            else:
                arr[i] = 0

        # return findSubarraySum(arr,n,0)
        # print(arr,n)

        freq = {}

        s = 0
        res = 0

        for i in arr:
            s += i

            if s == 0:
                res += 1

            if s in freq:
                res += freq[s]

            freq[s] = freq.get(s, 0)+1

        return res


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x, y = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))

        ans = Solution().sameOccurrence(arr, n, x, y)
        print(ans)
        tc -= 1

# } Driver Code Ends
