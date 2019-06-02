a = 34512423561108014234
b = 115792089210356248762697446949407573530086143415290314195533631308867097853951


def erweiterterEuklid(a, b):
    if a == 0:
        return b, 0, 1
    else:
        ggT, x, y = erweiterterEuklid(b % a, a)
        return ggT, y - (b // a) * x, x


def multiplikativeInverse(a, b):
    ggT, x, y = erweiterterEuklid(a, b)
    if ggT == 1:
        return x % b


print("Größter gemeinsamer Teiler: " + str(erweiterterEuklid(a, b)))
print("Multiplikatives Inverses: " + str(multiplikativeInverse(a, b)))
print("Probe ergibt ggT: " + str((multiplikativeInverse(a, b) * a) % b))

