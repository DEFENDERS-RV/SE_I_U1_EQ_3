import random

def matriz(row, col):
    matriz = [[0 for col in range(col)] for row in range(row)]
    for row in range(row):
        for col in range(col):
            matriz [row] [col] = random.randint(0,1)
    return matriz

if __name__ == "__main__":
    row = int(input("Ingrese fila: "))
    col = int(input("Ingresa columna: "))
    print(matriz(row, col))