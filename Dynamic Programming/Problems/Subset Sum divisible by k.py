def recursive_answer(arr, n, m, s):

    if s % m == 0 and s != 0:
        return True

    if n < 0:
        return False

    # O(2^n)
    return recursive_answer(arr, n-1, m, s+arr[n]) or recursive_answer(arr, n-1, m, s)


def optimised_answer(arr, n, m):

    st = {0}
    for i in arr:
        temp_set = set()
        for j in st:
            if (i+j) % m == 0:
                return True
            temp_set.add((i+j) % m)
        st = st.union(temp_set)
    return False


arr = list(map(int, input().split()))
n = len(arr)
m = int(input())

print(recursive_answer(arr, n-1, m, 0))
print(optimised_answer(arr, n, m))
