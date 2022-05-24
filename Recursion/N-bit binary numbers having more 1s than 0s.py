
def answer(ones, zeros, n, op, res):
    if n == 0:
        res.append(op)
        return

    if ones > zeros:
        op1 = op+"1"
        op2 = op+"0"
        answer(ones+1, zeros, n-1, op1, res)
        answer(ones, zeros+1, n-1, op2, res)
    else:
        op1 = op+"1"
        answer(ones+1, zeros, n-1, op1, res)


def NBitBinary(n):
    res = []
    answer(0, 0, n, "", res)
    return list(res)


print(NBitBinary(int(input())))
