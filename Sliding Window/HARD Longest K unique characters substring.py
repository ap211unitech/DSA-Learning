
# PROBLEM - https://practice.geeksforgeeks.org/problems/longest-k-unique-characters-substring0853/1

def longestKSubstr(s, k):
    i, j = 0, 0
    unique = dict()
    res = -1

    while(j < len(s)):
        unique[s[j]] = unique.get(s[j], 0)+1
        if len(unique.keys()) < k:
            j += 1
        elif len(unique.keys()) == k:
            res = max(res, j-i+1)
            j += 1
        else:
            while(len(unique.keys()) > k):
                unique[s[i]] -= 1
                if unique[s[i]] == 0:
                    del unique[s[i]]
                i += 1
            j += 1
    return res


s = input()
k = int(input())
print(longestKSubstr(s, k))
