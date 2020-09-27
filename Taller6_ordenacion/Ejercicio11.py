import random #Importe esto para desordenar la lista que creé

def quicksort(lista):
    izq = []
    der = []
    centro = [] #siempre sera de un elemento
    if len(lista) > 1:
        pivote = lista[0]
        for i in lista:
            if i < pivote:
                izq.append(i)
            elif i == pivote:
                centro.append(i)
            else:
                der.append(i)
        return quicksort(izq) + centro + quicksort(der)
    else:
        return lista 

#Para no escribir elemento por elemento haré lo siguiente = Declarar las listas, llenarlas con for, y desordenarlas 
listaA = []
for i in range(1, 100):
    listaA.append(2*i)  #A contendra solo numeros pares
random.shuffle(listaA, random.random) 

listaB = []
for i in range(1,60):
    listaB.append((2*i)-1) #B contendra solo numeros impares
random.shuffle(listaB, random.random)

listaC = listaA + listaB

#Esto son solo constantes para no tener que escribir lo mismo siempre y ahorrar codigo
imprimir = "Se desea ordenar la siguiente lista "
ordenada= "La lista ya ordenada: "

print("INICIO DE LA EJECUCION EJERCICIO 11")
#Lo mismo con este for, para ahorrar codigo escribiendo uno por uno cada lista 
for i in range(3):
    print("")
    if i == 0:
        print(imprimir, "de numeros pares: ")
        print(listaA)
        print("")
        print(ordenada)
        print(quicksort(listaA))
    elif i == 1:
        print(imprimir, "de numeros impares: ")
        print(listaB)
        print("")
        print(ordenada)
        print(quicksort(listaB))
    elif i == 2:
        print(imprimir, "union de las dos listas anteriores")
        print(listaC)
        print("")
        print(ordenada)
        print(quicksort(listaC))
print("")
print("Las listas son muy extensas asi que se recomienda subir hasta donde diga 'inicio de la ejecucion' para ver todo el proceso")
print("Por ultimo, como se puede observar, el resultado fue satisfactorio y se crea una hermosa lista de todos los N enteros hasta 118 (y de ahi sigue de 2 en 2 hasta 198)")
#Terminado
