#Import para ver los tiempos de ejecucion
import time

def countingsort(listaradix, exp1): 
   
    n = len(listaradix) 
   
    # los elementos de la salida(output) listaradixay que seran ordenados  
    output = [0] * (n) 
   
    #Inicializa el contador listaradixay como 0 
    count = [0] * (10) 
   
    #Guarda el numero de ocurrencias en count[] 
    for i in range(0, n): 
        index = (listaradix[i]/exp1) 
        count[int((index)%10)] += 1
   
    # Cambia el count[i] para que count[i] ahora contenga la verdadera posicion de su digito en la salida listaradixay
    for i in range(1,10): 
        count[i] += count[i-1] 
   
    # Construye la salida listaradixay 
    i = n-1
    while i>=0: 
        index = (listaradix[i]/exp1) 
        output[ count[ int((index)%10) ] - 1] = listaradix[i] 
        count[int((index)%10)] -= 1
        i -= 1
   
    #Copiando la salida de listaradixay hacia listaradix[] por lo que listaradix ahora tiene numeros ordenados
    i = 0
    for i in range(0,len(listaradix)): 
        listaradix[i] = output[i] 
 
# Metodo para hacer el radixsort
def radixsort(listaradix):
 
    # Encuentra el valor maximo para conocer el numero de digitos
    max1 = max(listaradix)
 
    # Hace counting sort para cada digito; notar que en vez de pasar el numero del digito, es exp el que se pasa
    # exp es 10^i donde i es el actual numero del digito
    exp = 1
    while max1/exp > 0:
        countingsort(listaradix,exp)
        exp *= 10
 


#Metodo de Binsort/bucketsort
def insertion_sort(bucket):
    for i in range (1, len (bucket)):
        var = bucket[i]
        j = i - 1
        while (j >= 0 and var < bucket[j]):
            bucket[j + 1] = bucket[j]
            j = j - 1
        bucket[j + 1] = var

def bucket_sort(n_cubetas):
    # Encuentra el valor maximo en la lista y usa el largo de la lista  para determinar que valor de la lista ira hacia una cubeta 
    max_value = max(n_cubetas)
    size = max_value/len(n_cubetas)

    #Crea una lista de cubetas vacias (donde n) es el numero de cubetas introducidas 
    buckets_list= []
    for x in range(len(n_cubetas)):
        buckets_list.append([]) 

    # Pone elementos listados dentro de diferentes cubetas, segun su tamaño
    for i in range(len(n_cubetas)):
        j = int (n_cubetas[i] / size)
        if j != len (n_cubetas):
            buckets_list[j].append(n_cubetas[i])
        else:
            buckets_list[len(n_cubetas) - 1].append(n_cubetas[i])

    # Ordena elementos entre las cubetas usando el metodo de insercion
    for z in range(len(n_cubetas)):
        insertion_sort(buckets_list[z])
            
    #Concatena las cubetas con los elementos ordenados hacia una unica lista 
    final_output = []
    for x in range(len (n_cubetas)):
        final_output = final_output + buckets_list[x]
    return final_output


listaradix = [ 45,23,51,23,36,21,623,4,8,1,10,23,15,18,50,23]
print("Se ordenara esta lista usando el metodo radixsort: ", listaradix)
print("")
start_time = time.time()
radixsort(listaradix)
print(listaradix)
print("Tarda--- %s segundos---" %(time.time()-start_time))

print("")
print("Ahora ordenando la misma lista con el metodo binsort/bucket sort: ")
print("")
start_time = time.time()
listabin = [ 45,23,51,23,36,21,623,4,8,1,10,23,15,18,50,23]
print(bucket_sort(listabin))
print("Tarda--- %s segundos---" %(time.time()-start_time))
print("Como conclusion el metodo por cubeta/bucket es mucho mas rapido que el ordenamiento radix")
print("COMO NOTA: la explicacion de cada metodo y declaracion esta en comentarios del codigo (nada de copiar y pegar, todo traducido por mi a mano; ya que estos ordenamientos no son de mi autoria)")
#Terminado