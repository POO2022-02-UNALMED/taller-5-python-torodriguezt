from animal import Animal

class Anfibio(Animal):
    
    ranas = 0
    salamandras = 0
    
    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self.__listado = []
        self.__colorPiel = colorPiel
        self.__venenoso = venenoso
        Animal.anfibio += 1
        
    def cantidadAnfibios(self):
        return len(self.__listado)
    
    def crearRana(self, nombre, edad, genero):
        rana = Anfibio(nombre, edad, "selva", genero, "rojo", True)
        self._listado.append(rana)
        Anfibio.ranas += 1
    
    def crearSalamandra(self, nombre, edad, genero):
        salamandra = Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)
        self._listado.append(salamandra)
        Anfibio.salamandras += 1
    
    def setListado(self, listado):
        self.__listado = listado
        
    def getListado(self):
        return self.__listado
    
    def setColorPiel(self, colorPiel):
        self.__colorPiel = colorPiel
        
    def getColorPiel(self):
        return self.__colorPiel
    
    def setVenenoso(self, venenoso):
        self.__venenoso = venenoso
        
    def getVenenoso(self):
        return self.__venenoso