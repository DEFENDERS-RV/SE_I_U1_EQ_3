import random

def generarLista(size):
    return [random.randint(0,1) for _ in range(size)]

if __name__ == "__main__":
    size = int(input("Ingrese tama;o de la lista: "))
    print(generarLista(size))
