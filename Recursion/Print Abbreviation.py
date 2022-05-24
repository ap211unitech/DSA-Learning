def answer(s, res, count, pos):

    if pos == n:
        if count == 0:
            print(res)
        else:
            print(res+str(count))
        return

    if count > 0:
        answer(s, res+str(count)+s[pos], 0, pos+1)
    else:
        answer(s, res+s[pos], 0, pos+1)
    answer(s, res, count+1, pos+1)


s = input()
n = len(s)
answer(s, "", 0, 0)
