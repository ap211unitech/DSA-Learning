# Minimum platforms required for all trains

arrive = list(map(int, input().split()))
depart = list(map(int, input().split()))

# Algo 
# We are checking when departure time is greater than arrival time, then we increase j pointer point to depart arr

n = len(arrive)
arrive.sort()
depart.sort()

i = 1
j = 0
plat = 1
res = 1
while(i < n and j < n):
    if arrive[i] <= depart[j]:
        plat += 1
        i += 1
    else:
        plat -= 1
        j += 1
    res = max(res, plat)
print(res)