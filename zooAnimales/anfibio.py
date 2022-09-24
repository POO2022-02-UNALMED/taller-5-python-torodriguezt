from zooAnimales.animal import Animal

class Anfibio(Animal):
    
    __listado = []
    ranas = 0
    salamandras = 0
    
    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self.__colorPiel = colorPiel
        self.__venenoso = venenoso
        Animal.anfibio += 1
        
    @classmethod
    def cantidadAnfibios(cls):
        return len(cls.__listado)
    
    @classmethod
    def crearRana(cls, nombre, edad, genero):
        rana = Anfibio(nombre, edad, "selva", genero, "rojo", True)
        cls.__listado.append(rana)
        cls.ranas += 1
    
    @classmethod
    def crearSalamandra(cls, nombre, edad, genero):
        salamandra = Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)
        cls.__listado.append(salamandra)
        cls.salamandras += 1
    
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
        
    def isVenenoso(self):
        return self.__venenoso
    