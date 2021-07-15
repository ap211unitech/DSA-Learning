# Would k hotel room be sufficient for all guests

arrive = list(map(int, input().split()))
depart = list(map(int, input().split()))
k = int(input())

#  Algo
# We will sort the array and manage count
n = len(arrive)
l = []
for i in range(n):
    l.append([arrive[i], 1])
    l.append([depart[i], 0])
l.sort()
active_rooms = 0
res = 0
for i in range(len(l)):
    if l[i][1] == 1:
        res += 1
    else:
        res -= 1
    active_rooms = max(active_rooms, res)
print(k >= active_rooms)

# Alternative
# n = len(arrive)
# arrive.sort()
# depart.sort()

# for i in range(n):
#     if i+k < n and arrive[i+k] < depart[i]:
#         print(0)
#         break
# print(1)
