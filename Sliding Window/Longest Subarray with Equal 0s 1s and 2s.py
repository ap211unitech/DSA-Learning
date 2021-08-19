
# PROBLEM - https://practice.geeksforgeeks.org/problems/equal-0-1-and-23208/1#

def getSubstringWithEqual012(s):

    arr = [int(i) for i in s]

    freq = {}
    res = 0

    zero, one, two = 0, 0, 0

    for i in arr:

        if i == 0:
            zero += 1
        elif i == 1:
            one += 1
        else:
            two += 1

        temp = (one-zero, two-one)

        if temp == (0, 0):
            res += 1

        if temp in freq:
            res += freq[temp]

        freq[temp] = freq.get(temp, 0)+1

        # print(freq)

    return res


s = input()
print(getSubstringWithEqual012(s))
