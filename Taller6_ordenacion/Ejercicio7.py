import time
def encontrarnegativos(lista):
    negativos = []
    for i in range(len(lista)):
        if lista[i] < 0:
            negativos.append(lista[i])
    return negativos

lista = [5, -1, 2, 6, -2, -5, 3, -3, -8, 10]
print("Se tiene la lista ", lista, " Y sus negativos son: ")
start_time = time.time()
print(encontrarnegativos(lista))
print("Tarda--- %s segundos---" %(time.time()-start_time))
print("El peor de los casos seria si todos los elementos de la lista fueran negativos ya que toca hacer append a todo")
lista2 = [-5, -1, -2, -6, -2, -5, 3, -3, -8, -10]
print("Ensayando este caso con la misma lista pasada, pero siendo todos negativos: ")
start_time = time.time()
print(encontrarnegativos(lista2))
print("Tarda--- %s segundos---" %(time.time()-start_time))
#Terminado