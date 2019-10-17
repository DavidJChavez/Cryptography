# Dados los primos p y q, encontrar el primo
# P* = n(p*q)+1 donde n es par.

from sympy import isprime

# Funciones para inverso multiplicativo
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

# Funciones para cada pregunta
def question1(p, q):
    n = 2
    i = 0
    primeS = n*p*q+1
    print("\nP* = ({0})({1})({2}) + 1 = {3}".format(n, p, q, primeS))
    while not isprime(n*p*q + 1):
        i += 1
        n = (i+1)*2
        P = n*p*q+1
        print("P* = ({0})({1})({2}) + 1 = {3}".format(n, p, q, primeS))
    return n, primeS

def question2(alpha, p, q, n, mod):
    while True:
        a = pow(alpha, p * q, mod)
        b = pow(alpha, 2 * p, mod)
        c = pow(alpha, 2 * q, mod)
        print("==============================")
        print("{0} ^ ({1})({2}) mod {3} = {4}".format(alpha, p, q, mod, a))
        print("{0} ^ ({1})({2}) mod {3} = {4}".format(alpha, 2, p, mod, b))
        print("{0} ^ ({1})({2}) mod {3} = {4}".format(alpha, 2, q, mod, c))
        print("==============================")
        if a != 1 and b != 1 and c != 1:
            return alpha
        alpha += 1

def question3(alpha, a, P, text, k):
    B = pow(alpha, a, P)
    print("\nB = ({0})^{1} mod {2} = {3}\n".format(alpha, a, P, B))
    y1 = pow(alpha, k, P)
    print("y1 = {0} ^ {1} mod {2}".format(alpha, k, P))
    print("y1 = {0}\n".format(y1))
    y2 = pow(text * pow(B, 24), 1, P)
    print("y2 = {0}*({1}) ^ {2} mod {3}".format(text, alpha, k, P))
    print("y2 = {0}\n".format(y2))
    print("Ek(x, k) = (y1, y2) = ({0}, {1})\n".format(y1, y2))
    y1pow = pow(y1, a, P)
    inverse = modinv(y1pow, P)
    decrypt = pow(y2*inverse, 1, P)
    print("d(y1, y2) = y2 * (y1 ^ a) ^ -1 mod P")
    print("d(y1, y2) = {0} * ({1} ^ {2}) ^ -1 mod {3}".format(y2, y1, a, P))
    print("d(y1, y2) = {0} * ({1}) ^ -1 mod {2}".format(y2, y1pow, P))
    print("d(y1, y2) = {0} * {1} mod {2}".format(y2, inverse, P))
    print("d(y1, y2) = {0}\n".format(decrypt))


if __name__ == "__main__":
    print("Examen B")
    print("Pregunta 1")
    p = int(input("Valor p: "))
    q = int(input("Valor q: "))
    n, primeS = question1(p, q)
    print("n = " + str(n) + "\n")

    alpha = int(input("Valor alpha: "))
    alpha = question2(alpha, p, q, n, primeS)
    print("Alpha generador: " + str(alpha) )

    a = int(input("Valor llave privada (a): "))
    text = int(input("Valor texto plano (text): "))
    k = int(input("Valor k: "))
    question3(alpha, a, primeS, text, k)
