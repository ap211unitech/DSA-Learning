
# PROBLEM - https://practice.geeksforgeeks.org/problems/count-number-of-substrings4528/1

def count_with_atmost_k_diffrent_integers(arr, k, n):

    freq = {}

    i = 0
    j = 0
    res = 0

    while(i < n):
        freq[arr[i]] = freq.get(arr[i], 0)+1

        while(len(freq) > k):
            freq[arr[j]] -= 1
            if freq[arr[j]] == 0:
                del freq[arr[j]]
            j += 1

        res += i-j+1
        i += 1

    return res


class Solution:
    def substrCount(self, s, k):
        nums = [i for i in s]
        n = len(nums)
        return count_with_atmost_k_diffrent_integers(nums, k, n)-count_with_atmost_k_diffrent_integers(nums, k-1, n)
