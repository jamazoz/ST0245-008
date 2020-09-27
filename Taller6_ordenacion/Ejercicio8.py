def omerge(lista):
    print("Dividir ",lista)
    if len(lista)>1:
        mitad = len(lista)//2
        izq = lista[:mitad]
        der = lista[mitad:]
        ## LLamada recursiva para cada lista 
        omerge(izq)
        omerge(der)
        i,j,k = 0,0,0
        while i < len(izq) and j < len(der):
            if izq[i] < der[j]:
                lista[k]=izq[i]
                i=i+1
            else:
                lista[k]=der[j]
                j=j+1
            k=k+1
        while i < len(izq):
            lista[k]=izq[i]
            i=i+1
            k=k+1


        while j < len(der):
            lista[k]=der[j]
            j=j+1
            k=k+1
    print("Mezclar ",lista)


lista = [21, 1, 26, 45, 29, 28, 2, 9, 16, 49, 39, 27, 43, 34, 46, 40]
print("Usando el codigo visto en clase para la lista ",lista)
omerge(lista)
print(lista)
print("")
print("Arriba se habrá podido apreciar todo el proceso que realiza el algoritmo")
print("Mostrandonos que, despues de 3 llamadas el algoritmo habrá dividido la parte izquierda hasta [21,1] ")
print("Esto sucede debido a que, lo primero que hace el metodo es llamarse a sí mismo para divirse en la izquierda, cosa que hará hasta que solo quede 1 elemento en izquierda, y 1 en derecha para intercambiarlos")
print("")
print("Como es una funcion recursiva que se divide a la mitad cada vez, si la lista es muy larga realizará muchos pasos, como en este caso miramos los 3 primeros pasos de una lista extensa, se puede apreciar que no alcanza a ordenar nada todavia")
#Terminado