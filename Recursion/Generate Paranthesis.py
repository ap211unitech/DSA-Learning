def isValid(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                return False
    return stack == []


def generate(n, op, res):

    if n == 0:
        res.append(op)
        return op

    op1 = "("+op
    op2 = ")"+op

    generate(n-1, op1, res)
    generate(n-1, op2, res)


def generateParenthesis(n):
    res = []
    generate(2*n, "", res)

    return [i for i in res if isValid(i)]


n = int(input())

print(generateParenthesis(n))
