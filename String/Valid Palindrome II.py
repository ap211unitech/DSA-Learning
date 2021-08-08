
# Problem - https://leetcode.com/problems/valid-palindrome-ii/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True

        n = len(s)

        l = 0
        r = n-1

        while(l < r):
            if s[l] != s[r]:
                delete_l = s[l+1:r+1]
                delete_r = s[l:r]
                return delete_l == delete_l[::-1] or delete_r == delete_r[::-1]
            l += 1
            r -= 1

        return True
