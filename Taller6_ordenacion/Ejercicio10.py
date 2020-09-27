def busquedamatriz(lista, elemento):
    encontrado = False
    for i in range(len(lista)):
        for j in range(len(lista)):
            if(lista[i][j] == elemento):
                encontrado = True
    if encontrado == True:
        return "Si esta en la lista"
    else:
        return "No se encuentra en la lista"

print("Inicio de la ejecucion EJERCICIO 11")
x = [[1,2,2,2,3,4], [1,2,3,3,4,5],[3,4,4,4,4,6],[4,5,6,7,8,9]]
print("Dada la siguiente lista ya declarada: ")
print(x)
buscar = int(input("Ingrese el elemento a buscar: "))
print(busquedamatriz(x, buscar))
print("")

matriz = []
print("Ahora se hará lo mismo con una matriz que el usuario mismo llena")
print("Recordar que son 4 filas y 6 columnas: ")
for i in range(4):
    matriz.append([0]*6)
for f in range(4):
    for c in range(6):
        matriz[f][c] = int(input("Elemento fila: %d, columna: %d : " % (f+1,c+1)))

print("Su matriz obtenida es: ")
for i in range(4):
    print("[", end= "")
    for j in range(6):
        print(matriz[i][j] , end=" ")
    print("]" ,end = "")
    print("")
print("")
buscar = int(input("Ingrese el elemento a buscar: "))
print(busquedamatriz(matriz, buscar))
#Terminado