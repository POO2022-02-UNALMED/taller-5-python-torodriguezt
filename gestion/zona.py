class Zona:
    
    def __init__(self,nombre, zoo):
        self.__nombre = nombre
        self.__zoo = zoo
        
    def agregarAnimales(self,especie):
        self.__animales.append(especie)
        
    def cantidadAnimales(self):
        return len(self.__animales)
    
    def setNombre(self, nombre):
        self.__nombre = nombre
        
    def getNombre(self):
        return self.__nombre
    
    def setZoo(self, zoo):
        self.__zoo = zoo
        
    def getZoo(self):
        return self.__zoo
    
    def setAnimales(self,animales):
        self.__animales = animales
        
    def getAnimales(self):
        return self.__animales