
# Problem - https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/

def minimumSwap(s1, s2):
    xy, yx = 0, 0
    for i, j in zip(s1, s2):
        if i == "x" and j == "y":
            xy += 1
        elif i == "y" and j == "x":
            yx += 1

    if (xy % 2+yx % 2) % 2 == 1:
        return -1

    return xy//2+yx//2+xy % 2+yx % 2


print(minimumSwap(input(), input()))
