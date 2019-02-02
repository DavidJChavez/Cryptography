# Modular Multiplication Table
import numpy as np

# Imprime matriz
def pmat(matrix):
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in matrix]))

# Return an int array
def multiples(number, top):
    multi = number
    array = []
    while multi < top:
        array.append(multi)
        multi += number
    # print("Multiples: " + str(array))
    return array

def multiply(module, matrix):
    for x in range(1, len(matrix[0])):
        for y in range(1, len(matrix[0])):
            matrix[x][y] = (matrix[0][y]*matrix[x][0])%module
    return matrix

# Return an int array
def zarray(numbers):
    zn = list(range(1, numbers[0]))
    for x in numbers[1:]:
        for y in multiples(x, numbers[0]):
            zn.remove(y)

    print("Zn*" + str(numbers[0]) + ": " + str(zn))
    
    matrix = np.zeros(shape=(len(zn) + 1, len(zn) + 1), dtype=int, )
    for x in range(1, len(zn) + 1):
        matrix[0][x] = zn[x-1]
        matrix[x][0] = zn[x-1]
    # pmat(matrix)
    matrix = multiply(numbers[0], matrix)

    pmat(matrix)

    return zn

def main():
    numbers = input("Numbers: ")
    numbers = numbers.split(" ")
    numbers = [ int(x) for x in numbers ]
    zarray(numbers)

if __name__ == '__main__':
    main()