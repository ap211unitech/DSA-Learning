
# This problem is also known as flood fill

# PROBLEM https://practice.geeksforgeeks.org/problems/rat-in-a-maze-problem/1#

def answer(arr, row, col, path_so_far, visited, res):
    if row < 0 or col < 0 or row >= len(arr) or col >= len(arr[0]) or arr[row][col] == 0 or visited[row][col] == True:
        return

    if row == len(arr)-1 and col == len(arr[0])-1:
        res.append(path_so_far)
        return

    visited[row][col] = True
    answer(arr, row-1, col, path_so_far+'U', visited, res)
    answer(arr, row+1, col, path_so_far+'D', visited, res)
    answer(arr, row, col-1, path_so_far+'L', visited, res)
    answer(arr, row, col+1, path_so_far+'R', visited, res)
    visited[row][col] = False


class Solution:
    def findPath(self, arr, n):
        visited = [[False for i in range(n)] for j in range(n)]
        res = []
        answer(arr, 0, 0, "", visited, res)
        res.sort()
        return res


arr = [
    [1, 0, 0, 0],
    [1, 1, 0, 1], # 0 for obstacle
    [1, 1, 0, 0],
    [0, 1, 1, 1],
]

ob = Solution()
print(ob.findPath(arr, len(arr)))
