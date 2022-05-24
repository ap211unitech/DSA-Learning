
def countRev(s):

    if len(s) % 2 == 1:
        return -1

    stack = []

    for i in s:
        if i == "{":
            stack.append(i)
        else:
            if stack and stack[-1] == "{":
                stack.pop()
            else:
                stack.append(i)

    size = len(stack)

    count = 0
    while(stack and stack[-1] == "{"):
        stack.pop()
        count += 1

    return (count % 2+size//2)


print(countRev("}{{}}{{{"))

print(countRev("{{}{{{}{{}}{{"))
