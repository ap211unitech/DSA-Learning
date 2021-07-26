
def answer(s, i, j, res):
    if i > j:
        return

    if s[i] == s[j] and j != i:
        res.add(s[i:j+1])

    answer(s, i+1, j, res)
    answer(s, i, j-1, res)


s = input()
res = set()
answer(s, 0, len(s)-1, res)
res = list(res)
res += [i for i in s]
print(res)
