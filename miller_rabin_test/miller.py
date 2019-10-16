# Miller Rabin Test

def isCongruent(a, b, m):
    if a == b or ( abs(a - b) % m ) == 0:
        return True
    else:
        return False

# int n, int a (default: 2)
# return int k, int m
def getKM(n, a=2):
    m = n-1
    k = 0
    while m%a == 0:
        k += 1
        m /= a
    return (int(k), int(m))


def miller(a, n, _iter):
    k, m = getKM(n)
    b = (a**m)%n
    isPrime = bool
    if isCongruent(b, 1, n):
        isPrime = True
    else:
        for x in range(0, _iter):
            if isCongruent(b, -1, n):
                isPrime = True
            

if __name__ == "__main__":
    a = int(input("Value a: "))
    n = int(input("Value n: "))
    _iter = int(input("Iterations: "))
    if miller(a, n, _iter):
        print("Prime")
    else:
        print("Composit")