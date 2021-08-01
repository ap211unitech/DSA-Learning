
def solve(n, ans, res):
    if len(n) == 0:
        res.append(ans)
        return

    if n[0] == "0":
        return

    if len(n) == 1:
        if n == '0':
            return
        else:
            ans = ans+chr(int(n[0])+96)
            print(ans)
            return
    else:
        if n[0] == '0':
            return
        else:
            solve(n[1::], ans+chr(int(n[0])+96), res)
            if int(n[0:2]) >= 1 and int(n[0:2]) <= 26:
                solve(n[2::], ans+chr(int(n[0:2])+96), res)


n = input()
if len(n) == 0 or n.isspace():
    print()
    exit()

res = []
solve(n, "", res)
