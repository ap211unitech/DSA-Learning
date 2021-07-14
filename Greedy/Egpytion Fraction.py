import math

#  A fraction written as sum of unit fractions ( 1/k type)

def getFractions(nr, dr):
    res = []

    while(nr != 0):
        x = math.ceil(dr/nr)
        res.append(x)
        nr = nr*x-dr
        dr = dr*x

    print(res)


a, b = map(int, input().split())
getFractions(a, b)
