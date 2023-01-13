
def fibo(a):
    if a == 0:
        return 0
    elif a == 1:
        return 1
    else:
        return fibo(a - 1) + fibo(a - 2)


print(fibo(40))



def ord(n):
    if len(n) > 2:
        g,d = split(n)
        rg = ord(g)
        rd = ord(d)

    rejoindre(rg, rd)