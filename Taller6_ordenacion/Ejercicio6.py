futbolistasTup = [(1, "Casillas"), (15, "Ramos"), (3, "Pique"), (5, "Puyol"), (11, "Capdevila"), (14, "Xabi Alonso"), (16, "Busquets"), (8, "Xavi Hernandez"), (18, "Pedrito"), (6, "Iniesta"), (7, "Villa")]
print("Se tiene la siguiente lista '" ,futbolistasTup, "' la cual se ordenara")
futbolistasTup.sort(key=lambda futbolista: futbolista[1])
print(futbolistasTup)
print("RESPUESTAS")
print("A. Se puede apreciar que se ordenó por numero, no por nombre y que mantuvo las tuplas tal como estaban sin mezclar numero con nombre")
print("B. El key crea una funcion lambda o anonima, que no se relaciona a un vinculador, y crea otra lista ordena segun numero que elijamos, si se pone 0 ordenara teniendo en cuenta el primer elemento de la tupla, con 1 ordenara segun el segundo elemento, y así sucesivamente")
print("C. Despues de aplicar el metodo al punto 1, 3 y 4, concluyo que, en todos salio error 'int is not suscriptable' y que este metodo solo funciona para tuplas o superior (mas de 1 elemento agrupado), borre esa parte del codigo en los ejercicios para no tener el error")

inventosTup = [(60, "HTC Vive pro eye"), (40, "Postmates Serve"),(70,"Away backpack"),(85,"Lightyear One"),(90,"BML100PI"),(20, "CUbE"),(86,"Elevate Walking Car"),(80, "ECOncrete")]
#Terminado