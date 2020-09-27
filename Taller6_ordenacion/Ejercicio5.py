#Hice dos metodos, uno hecho por las herramientas que python brinda, y el otro intentando hacer todo con ciclos y listas
import time 
#Metodouno
def contarvotos(lista):
    return {i: lista.count(i) for i in lista}


listaacontar= [5 , 4, 3, 5, 1, 6, 2, 8, 9, 1, 2, 3, 5, 5, 4, 2]
print("Con el metodo uno")
print("")
print(listaacontar ," Dada esta lista: ")
start_time = time.time()
contado= contarvotos(listaacontar)
maximo=max(contado, key=contado.get)
print("Tarda--- %s segundos---" %(time.time()-start_time))
print("El valor mas repetido es el ",maximo," con ",contado[maximo]," veces")
print("La complejidad de este algoritmo es: n^2")

def contarvotosdos(lista):
    listausar = []
    for i in range(len(lista)): #n + n-1 + n-1 = 3n - 2
        if not lista[i] in listausar:
            listausar.append(lista[i]) #aqui llevo los elementos que no son repetidos a la otra lista
    
    votos = []
    for i in range(len(listausar)): #n + n = 2n #Se llena la lista de votos con 0, solo para declarar el largo de la lista
        votos.append(0)

    for i in range(len(lista)): # n + n + n^2 + n = 3n + n^2 + 1 
        for j in range(len(listausar)):
            if lista[i] == listausar[j]:
                votos[j] = int(votos[j] +1 )
    maximo = max(votos, key= int)     # 3n - 2  + 2n + 3n + n^2 =  n^2 + 8n  
    print(listausar, " Candidatos a votaciones")
    print(votos, " Votos por cada uno")
    print("Siendo la mayor cantidad de votos : ", end="")
    return maximo
    #Se puede hacer que tambien retorne el mayor votado, pero para eso necesitaria un for extra si no se quiere hacer 
    #lo mismo del metodouno
print("")
print("Con el metodo dos: ")
listaacontar= [5, 4, 3, 5, 1, 6, 2, 8, 9, 1, 2, 3, 5, 5, 4, 2]
print(listaacontar ," Dada esta lista: ")
print("Se mostrara los datos para votar, y abajo sus respectivos votos: ")
start_time = time.time()
print(contarvotosdos(listaacontar))
print("Tarda--- %s segundos---" %(time.time()-start_time))
print("La complejidad del segundo metodo es n^2+n")
#Terminado