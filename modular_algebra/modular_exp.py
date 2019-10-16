# Modular exponetiation

def mpow(b, e, m):
    a = "{0:b}".format(e)
    print("Bin: " + a)
    c = 1
    for i in reversed(range(len(a))):
        if a[i] == '1':
            c = (c*b)%m
        b = (b * b)%m
    return c
    

if __name__ == "__main__":
    print("Format: b ^ e mod m")
    base = int(input("b: "))
    exp = int(input("e: "))
    module = int(input("m: "))
    print("Result: " + str(mpow(base, exp, module)))