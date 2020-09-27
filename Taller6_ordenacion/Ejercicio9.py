class set:
    def __init__(self):
        self._theelements = list()

    def __len__(self):
        return(len(self._theelements))

    def __contains__(self,element):
        ndx = self._findposition(element)
        return ndx < len(self) and self._theElements[ndx] == element
    
    def add (self, element):
        if element not in self:
            ndx = self._findposition(element)
            self._theelements.insert(ndx,element)
    
    def remove(self,element):
        assert element in self, "El elemento tiene que estar en el set"
        ndx = self._findPosition(element)
        self._theelements.pop(ndx)

    def issubsetof(self,setb):
        for element in self:
            if element not in setb:
                return False
        return True
    #el resto de elementos van aqui

    #def __iter__(self):
       # return _SetIterator(self._theelements) se comenta ya que no esta el metodo SetIterator y provocaria error
    
    def _findposition(self,element):
        low = 0
        high = len(self) -1
        while low <= high:
            mid = (high+low)/2
            if self[mid] == element:
                return mid
            elif element < self[mid]:
                high = mid-1
            else:
                low = mid+1
        return low

print("Este codigo crea un set, es decir, una coleccion de datos unicos, parecido a una lista")
print("El init inicializa una lista; su complejidad es 1")
print("Len sirve para conocer el largo que tiene la lista; su complejidad es 1")
print("Contains sirve para ver si el set contiene un elemento especifico que el usuario busca; su complejidad es 4")
print("add añade un elemento nuevo al set; su complejidad es 3")     
print("remove remueve un elemento del set; su complejidad es 3")
print("issubsetof sirve para ver si algo es un subset de un elemento del set (Por ejemplo: un elemento del set es una lista, subsetof sirve para mirar si en esa lista hay un elemento que estamos buscando; su complejidad es 2n")
print("iter sirve para ver el iterador de el set; su complejidad es 1")
print("findposition sirve para que, al buscar un elemento del set retorne la posicion en la que se encuentra, pero no esta completo pues falta otro metodo que realice la llamada recursiva; su complejidad es 3n puesto que no esta completo el metodo") 
print("Con los metodos vistos hasta el momento se puede ver que la clase SET tiene una complejidad lineal de O(n)")      
#Terminado