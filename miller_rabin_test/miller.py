# Miller Rabin Test
import random

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


def miller(aArray, n):
    k, m = getKM(n)
    for a in aArray:
        b = pow(a,m,n)
        if isCongruent(b, 1, n):
            print("With a = " + str(a) + ", n is probably Prime")
        else:
            for _ in range(k):
                b = pow(b, 2, n)
                if isCongruent(b, -1, n):
                    print("With a = " + str(a) + ", n is probably Prime")
                    break
                elif isCongruent(b, 1, n):
                    print("With a = " + str(a) + ", n is probably Composite")
                    break
                elif _ == k-1:
                    print("N is probably Composite")
                    break

                
            

if __name__ == "__main__":
    a = []
    n = int(input("Value n: "))
    _iter = int(input("Iterations: "))
    for x in range(_iter):
        value = input("Value a "+ str(x+1) + " (r: rand): ")
        if value == 'r':
            a.append(int(random.randrange(2, n - 1)))
        else:
            a.append(int(value))
    miller(a, n)
