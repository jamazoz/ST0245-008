def burbuja(lista):
    for numpasada in range(len(lista)-1,0,-1):
        for i in range(numpasada):
            print(numpasada) #no debe ir, es solo para visualizar las pasadas
            if lista[i]>lista[i+1]:
                temp = lista[i]
                lista[i]=lista[i+1]
                lista[i+1] = temp
    return lista

def insercion(lista):
    num = 0
    for i in range(len(lista)):
        valorordenar = lista[i]
        while lista[i-1] > valorordenar and i > 0:
            num += 1
            print(num)
            lista[i], lista[i-1] = lista[i-1], lista[i]
            i = i - 1
    return lista

def seleccion(lista):
    for i in range(0, len(lista)):
        mas_pequeno= i  #almacenamos el valor mas pequeño de la posicion del vector a trabajar
        print(i)
        for j in range(i+1, len(lista)):
            if(lista[j] < lista[mas_pequeno]):
                mas_pequeno = j
        if min is not i:
            lista[i], lista[mas_pequeno] = lista[mas_pequeno] , lista[i]
    return lista

lista1= [47,3,21,32.56,92]
print("Metodo burbuja: ")
print(burbuja(lista1))
print("Metodo de insercion")
print(insercion(lista1))
print("Metodo de seleccion")
print(seleccion(lista1))

print("Como conclusion, despues de 2 pasadas si la lista queda como '[3,21,47,32,56,92]' se usó el método burbuja ya que en la pasada 1 comparó 47 con 3 y los intercambió, en la segunda pasada comparó 47 con 21 y lo intercambia, dando como resultado la anterior lista")
#Terminado