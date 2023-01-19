from Ejercicios import Ej3 as g

#obj = Ej3()
#int_obj = int(obj)
row = int(input("Ingrese fila: "))
col = int(input("Ingrese columna: "))
#su = [sum(i) for i in range(g.matriz(row, col))]
#peso = [for _ in range(g.matriz(row, col).count(1)]

print(g.matriz(row, col))
print(peso)

#----------

def getPeso(vector):
    return sum(vector)


Matriz = [
    [1,0,0,0],
    [1,1,1,0],
    [0,1,1,0],
    ]
print(Matriz)

#Calcular el promedio 
#Ordenando la matriz
#Matriz.sort(key = lambda vector:sum(vector) , reverse=True)
Matriz.sort(key = lambda vector:getPeso(vector) , reverse=True)
print(Matriz)


