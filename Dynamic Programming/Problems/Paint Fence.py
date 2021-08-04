
# Given a fence with n posts and k colors, find out the number of ways of painting the fence such that at most 2 adjacent posts have the same color. Since answer can be large return it modulo 10^9 + 7.

# Problem - https://practice.geeksforgeeks.org/problems/painting-the-fence3727/1

# Help - https://www.youtube.com/watch?v=ju8vrEAsa3Q&list=PL-Jc9J83PIiG8fE6rj9F5a6uyQ5WPdqKy&index=25


def solve(n, k):
    if n < 2:
        if k < n:
            return 0
        return k

    mod = 10**9+7
    last_two_same = [0 for i in range(n)]
    last_two_diffrent = [0 for i in range(n)]

    last_two_same[1] = k
    last_two_diffrent[1] = k*(k-1)

    for i in range(2, n):
        last_two_same[i] = last_two_diffrent[i-1] % mod
        last_two_diffrent[i] = (
            (k-1)*(last_two_diffrent[i-1]+last_two_same[i-1])) % mod

    return (last_two_diffrent[n-1]+last_two_same[n-1]) % mod


n, k = map(int, input().split())
print(solve(n, k))
