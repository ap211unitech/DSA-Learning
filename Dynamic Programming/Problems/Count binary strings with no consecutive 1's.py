
# This is same as "count binary strings with no consecutive 0's"
# This is same as "count binary strings with no consecutive 1's"


def countStrings(n):

    mod = 10**9+7
    count_zeros = 1  # for n=1
    count_ones = 1  # for n=1

    for i in range(2, n+1):
        new_count_zeros = (count_zeros) % mod+(count_ones) % mod
        new_count_ones = (count_zeros) % mod

        count_zeros = new_count_zeros
        count_ones = new_count_ones

    return ((count_zeros % mod)+(count_ones % mod)) % (10**9+7)


# Given a n
n = int(input())
print(countStrings(n))
