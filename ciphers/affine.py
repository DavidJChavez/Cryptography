alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
modulo = len(alphabet)

# Extendido de GCD, regresa "int"
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

# Regresa inverso multiplicativo modular (a^-1 mod m), regresa "int mod module"
def modinv(a, modulo):
    g, x, y = egcd(a, modulo)
    if g != 1:
        raise Exception('Inverso multiplicativo inexistente')
    else:
        return x % modulo

def cipher(a, b, word):
    ciphered_word = ""
    for x in word:
        ciphered_word += alphabet[(a*alphabet.find(x) + b)%modulo]
    return ciphered_word

def decipher(a, b, word):
    deciphered_word = ""
    for x in word:
        deciphered_word += alphabet[(modinv(a, modulo) * (alphabet.find(x) - b))%modulo]
    return deciphered_word

# Main
def main():
    option = ""
    while option != "E":
        option = input("[C]ipher, [D]ecipher, [E]xit: ").upper()
        if option == "C":
            a = int(input("A: "))
            b = int(input("B: "))
            word = input("Word: ").upper()
            print("Ciphered word: " + cipher(a, b, word))
        elif option == "D":
            a = int(input("A: "))
            b = int(input("B: "))
            word = input("Word: ").upper()
            print("Deciphered word: " + decipher(a, b, word))


if __name__ == '__main__':
    main()