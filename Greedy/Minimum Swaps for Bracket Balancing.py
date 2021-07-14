
# Visit - https://practice.geeksforgeeks.org/problems/minimum-swaps-for-bracket-balancing2704/1

def minimumNumberOfSwaps(s: str):

    s = [i for i in s]
    v = [i for i in range(len(s)) if s[i] == "["]

    ans = 0
    count = 0
    idx = 0

    for i in range(len(s)):
        if s[i] == "[":
            count += 1
            idx += 1
        else:
            count -= 1
            if count < 0:
                ans += v[idx]-i
                s[i], s[v[idx]] = s[v[idx]], s[i]
                count = 1
                idx += 1

    return ans
