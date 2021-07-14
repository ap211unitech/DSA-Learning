
# Visit https://practice.geeksforgeeks.org/problems/assign-mice-holes3053/1#

def assignMiceHoles(n, mice, holes):
    mice.sort()
    holes.sort()

    res = 0
    for i in range(n):
        res = max(abs(mice[i]-holes[i]), res)
    return res


print(assignMiceHoles(2, [4, 2], [1, 7]))
