def shell(lista):
    contadorsublistas = len(lista)//2
    while contadorsublistas > 0:
        for init in range(contadorsublistas):
            brechainsercion(lista, init, contadorsublistas)
        contadorsublistas = contadorsublistas // 2
    return lista


def brechainsercion(lista,init, brecha):
    for i in range(init + brecha, len(lista), brecha):
        actual = lista[i]
        pos = i
        while pos >= brecha and lista[pos-brecha]> actual:
            lista[pos] = lista[pos-brecha]
            pos = pos-brecha
        lista[pos] = actual

lista = [8, 43, 17, 6, 40, 16, 18, 97, 11, 7]
print("Teniendo una lista desordenada ", lista)
print("Se crea un intervalo =  n//2  tal que 10//2 = 5")
print("Se halla el elemento en la posicion del intervalo = 16, y lo compara con el elemento 5 posiciones atras = 8,  16 > 8 por lo tanto queda igual")
print("")
print("luego compara el siguiente al 16 = 18  con el siguiente al 8 = 43, 18 < 43 por lo tanto se intercambian, quedando tal que[8, 18, 17, 6, 40, 16, 43, 97, 11, 7] ")
print("Luego compara el proximo elemento a 43 = 97, con el proximo elemento a 18 = 17, 97 > 17, por lo tanto queda igual")
print("Compara despues el siguiente a 97 = 11, con el siguiente a 17 = 6, 11 > 6, por lo tanto queda igual")
print("por ultimo, Compara el siguiente a 11 = 7, con el siguiente a 6 = 40, 7 < 40, por lo tanto intercambia quedando  [8, 18, 17, 6, 7, 16, 43, 97, 11, 40] ")
print("")
print("Una vez terminado este primer recorrido actualiza el intervalo con el anterior intervalo como n = 5, 5//2 = 3 y vuelve a lo mismo" )
print("Elemento en la posicion 3 = 6, elemento 3 posiciones anterior = 8, 6 < 8, por ende se intercambia, quedando [6, 18, 17, 8, 7, 16, 43, 97, 11, 40]")
print("Sigue realizando estas comparaciones tal como se hizo anteriormente dando como resultado a todos los intercambios = [6, 7, 16, 8, 18, 11, 40, 97, 17, 43] ")
print("")
print("Luego tomara de nuevo el anterior intervalo para n = 3, 3//2 = 2 y repite el proceso esta vez comparando de a 2 espacios")
print("el elemento en la posicion 2 = 16, el elemento 2 posiciones atras = 6, 16 > 6, no intercambia, y vuelta a empezar")
print("Seguira haciendo el proceso hasta llegar a [6, 7, 16, 8, 18,11 ,17 ,43 ,40, 97] ")
print("")
print("Una vez terminado este proceso, repetirá lo de crear un nuevo intervalo usando el anterior como n = 2, 2//2 = 1")
print("Ahora se hara cambios de una posicion, estando en la posicion 1 = 7, y el elemento 1 posicion atras = 6, 7 > 6, no hay cambio")
print("Al terminar estas comparaciones estaria terminado el ordenamiento dando como resultado: ")
print(shell(lista))
#Terminado