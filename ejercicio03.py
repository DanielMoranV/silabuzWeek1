"""
Ejercicio 3: Dada la matriz, [[1,2,3],[4,5,6],[7,8,9]], calcule el promedio de la diagonal principal. Hint: Los 3 elementos de la diagonal son 1,5,9
"""
matriz = [[1,2,3],[4,5,6],[7,8,9]]
listadd=[]
for i in range(len(matriz)):
    listadd.append(matriz[i][i])
    print (matriz[i][i])

prom = sum(listadd)/len(matriz)

print (f"El promedio es: {prom}")