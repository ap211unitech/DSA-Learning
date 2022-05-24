
# Problem - https://leetcode.com/problems/valid-parenthesis-string/
# Hint - https://www.youtube.com/watch?v=KuE_Cn3xhxI

def checkValidString(s):
    n = len(s)

    open = []
    star = []

    for i in range(n):
        if s[i] == "(":
            open.append(i)
        elif s[i] == "*":
            star.append(i)
        else:
            if len(open) != 0:
                open.pop()
            elif len(star) != 0:
                star.pop()
            else:
                return False

    for i in range(len(open)-1, -1, -1):
        if star and star[-1] > open[i]:
            star.pop()
        else:
            return False

    return True


print(checkValidString(input()))
