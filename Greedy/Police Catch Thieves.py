
# Visit https://www.geeksforgeeks.org/policemen-catch-thieves/

arr = list(map(str, input().split()))  # list of 'P' and 'T'
k = int(input())

n = len(arr)

police = []
thief = []
for i in range(n):
    if arr[i] == "P":
        police.append(i)
    else:
        thief.append(i)

i = 0
j = 0
res = 0

while(i < len(police) and j < len(thief)):
    if abs(police[i]-thief[j]) <= k:
        res += 1
        i += 1
        j += 1
    elif police[i] < thief[j]:
        i += 1
    else:
        j += 1

print("Maximum thief can be caught: ", res)
