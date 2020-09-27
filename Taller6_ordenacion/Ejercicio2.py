import time 
def eliminarrepetidoordenado(lista):
    listasinrepetido =[]
    for i in range(len(lista)):
        if i == 0 or lista[i] != lista[i-1]:
            listasinrepetido.append(lista[i])
    return listasinrepetido

lista = [4,7,11,4,9,5,11,7,3,5]
lista.sort()
print("Teniendo la lista: " ,lista, " se eliminaran los repetidos")
start_time = time.time()
print(eliminarrepetidoordenado(lista))
print("Tarda--- %s segundos---" %(time.time()-start_time))
print("Esta claro que cuando esta ordenado es mucho mas eficiente, pero depende del metodo, por ejemplo en el que use para el ejercicio 1 seria mas rapido porque hace 1 comparacion menos")
#Terminado