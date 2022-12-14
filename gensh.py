from decimal import Decimal as D


def griv(rub):
    rub = D(rub)
    return D(rub / kurs)

def rubl(gri):
    gri = D(gri)
    return D(gri * kurs)

def percent(p, x):
    p = D(p)
    x = D(x)
    return D(x * (p / 100))

kurs = D(D(1352.78) / D(706.3))

s = rubl(706.30)
s = D(240)
for i in range(1, 51):
    if (s + percent(i, s)) * D(0.97) >= s and (s + percent(i, s)) * D(0.97) <= s + percent(17, s):
        price = D(s + percent(i, s))
        print(price, i, '%')
        print(price + percent(13, price))
        print('_____', price - s)

print(D(s + percent(D(3.1), s)) * D(0.97))