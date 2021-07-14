start = list(map(int, input().split()))
end = list(map(int, input().split()))

n = len(start)

l = [[start[i], end[i]] for i in range(n)]
l.sort(key=lambda x: x[1])

meeting = 1
i = 0
for j in range(1, n):
    if l[j][0] >= l[i][1]:
        meeting += 1
        i = j

print(meeting)
