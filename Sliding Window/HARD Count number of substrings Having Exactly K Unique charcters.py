
# PROBLEM - https://practice.geeksforgeeks.org/problems/count-number-of-substrings4528/1

def solnk1(s):

    res = 0
    n = len(s)
    i = 0
    freq = {}
    j = 0

    while(i < n):
        curr = s[i]
        freq[curr] = freq.get(curr, 0)+1

        if len(freq) == k:
            res += 1

        elif len(freq) > k:
            res += i-j

            while(len(freq) > k):
                freq[s[j]] -= 1
                if freq[s[j]] == 0:
                    del freq[s[j]]
                j += 1
        i += 1

        # print(freq,res)

    return res


class Solution:
    def substrCount(self, s, k):

        if k == 1:
            return solnk1(s)

        n = len(s)

        mapb = {}
        maps = {}

        ib = -1
        ism = -1
        j = -1

        res = 0

        while(True):

            f1, f2, f3 = False, False, False

            # Filling big Hash
            while(ib < n-1):
                f1 = True
                ib += 1
                curr = s[ib]
                mapb[curr] = mapb.get(curr, 0)+1

                if len(mapb) > k:
                    mapb[curr] -= 1
                    ib -= 1
                    if mapb[curr] == 0:
                        del mapb[curr]
                    break

            # Filling Small Hash
            while(ism < ib):
                f2 = True
                ism += 1
                curr = s[ism]
                maps[curr] = maps.get(curr, 0)+1

                if len(maps) > k-1:
                    maps[curr] -= 1
                    ism -= 1
                    if maps[curr] == 0:
                        del maps[curr]
                    break

            # Removing Elements
            while(j < ism):
                f3 = True
                if len(mapb) == k and len(maps) == k-1:
                    res += ib-ism

                j += 1
                curr = s[j]
                mapb[curr] -= 1
                if mapb[curr] == 0:
                    del mapb[curr]

                maps[curr] -= 1
                if maps[curr] == 0:
                    del maps[curr]

                if len(mapb) < k and len(maps) < k-1:
                    break

            if f1 == False and f2 == False and f3 == False:
                break

        return res
