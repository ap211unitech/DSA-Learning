def solve(arr, i, n, visited, res):

    if i >= n:
        print(res)
        return

    if visited[i] == True:
        solve(arr, i+1, n, visited, res)
    else:
        visited[i] = True
        solve(arr, i+1, n, visited, res+"("+arr[i]+") ")
        for j in range(i+1, n):
            if visited[j] == False:
                visited[j] = True
                solve(arr, i+1, n, visited, res+"("+arr[i]+" "+arr[j]+") ")
                visited[j] = False
        visited[i] = False


n = int(input())
arr = [str(i) for i in range(1, n+1)]
visited = [False for i in range(n)]
res = ""
solve(arr, 0, n, visited, res)
