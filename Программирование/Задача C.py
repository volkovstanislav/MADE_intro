import math
import itertools
from fractions import Fraction

# https://ru.stackoverflow.com/questions/1014237/
# Число сочетаний из k по n
def С(n, k):
    if 0 <= k <= n:
        nn = 1
        kk = 1
        for t in range(1, min(k, n - k) + 1):
            nn *= n
            kk *= t
            n -= 1
        return nn // kk
    else:
        return 0

MAX_VALUE = 64
mods = []
pows_sq = []
for i in range(0, MAX_VALUE):
    pows_sq.append([Fraction(1, int(math.pow(2, i)))] * (i + 1))
    mods.append([Fraction(С(i, k)) for k in range(0, i + 1)])

pows_sq = list(itertools.chain(*pows_sq))
mods = list(itertools.chain(*mods))

final_result = []
x = input()

for j in range(int(x)):
    res = []
    h = input()
    for k in range(int(h)):
        sf = list(map(int, input().split()))
        res.append(sf)

    res = list(itertools.chain(*res))
    s = Fraction(0)

    for (sc, p2, c) in list(zip(res, pows_sq, mods)):
        mul = sc * p2 * c
        s += mul
    final_result.append(s)

for res in final_result:
    if res.numerator != 0:
        print(res.numerator, res.denominator)
    else:
        print(res.numerator, 1)