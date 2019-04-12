# Session 1: Substitution cipher
# 1.1
# Author: David Josue Rodriguez Chavez
import string
alphabet = string.printable
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
            file = input("Data file name: ")
            data = ""
            with open(file + ".txt", 'r') as plaintext:
                data = plaintext.read()
            with open(file + ".afn", 'w') as ciphered_text:
                ciphered_text.write(cipher(a, b, data))
        elif option == "D":
            a = int(input("A: "))
            b = int(input("B: "))
            file = input("Data file name: ")
            data = ""
            with open(file + ".afn", 'r') as plaintext:
                data = plaintext.read()
            with open(file + ".txt", 'w') as ciphered_text:
                ciphered_text.write(decipher(a, b, data))


if __name__ == '__main__':
    main()