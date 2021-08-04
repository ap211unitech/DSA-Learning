# This is same as "count binary strings with no consecutive 0's"
# This is same as "count binary strings with no consecutive 1's"

def arrangeBuildings(n):

    mod = 10**9+7
    count_buildings = 1  # for n=1
    count_spaces = 1  # for n=1

    for i in range(2, n+1):
        new_count_buildings = (count_buildings) % mod+(count_spaces) % mod
        new_count_spaces = (count_buildings) % mod

        count_buildings = new_count_buildings
        count_spaces = new_count_spaces

    ans = ((count_buildings % mod)+(count_spaces % mod)) % (10**9+7)
    return (ans*ans) % mod


# Given a n
n = int(input())
print(arrangeBuildings(n))
