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
    # generate(n,n,"",res)

    return [i for i in res if isValid(i)]


# def generate(open, close, op, res):

#     if open == 0 and close == 0:
#         res.append(op)
#         return

#     if open != 0:
#         op1 = op+"("
#         generate(open-1, close, op1, res)

#     if close > open:
#         op2 = op+")"
#         generate(open, close-1, op2, res)


n = int(input())

print(generateParenthesis(n))

