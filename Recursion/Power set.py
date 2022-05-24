
def powerSet(arr, op, n, i, res):
    if i == n:
        res.append(op)
        return

    op1 = op
    op2 = op + arr[i]
    powerSet(arr, op1, n, i+1, res)
    powerSet(arr, op2, n, i+1, res)


arr = input()
res = []
powerSet(arr, "", len(arr), 0, res)
print(res)
