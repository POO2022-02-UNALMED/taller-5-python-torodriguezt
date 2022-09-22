from zooAnimales.animal import Animal
class Pez(Animal):
    
    salmones = 0
    bacalaos = 0
    
    def __init__(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas):
        super().__init__(nombre, edad, habitat, genero)
        self.__listado = []
        self.__colorEscamas = colorEscamas
        self.__cantidadAletas = cantidadAletas
        Animal.pez += 1
        
    def cantidadPeces(self):
        return len(self.__listado)

    def crearSalmon(self, nombre, edad, genero):
        salmon = Pez(nombre, edad, "oceano", genero, "rojo", 6)
        self._listado.append(salmon)
        Pez.salmones += 1
     
    def crearBacalo(self, nombre, edad, genero):
        bacalao = Pez(nombre, edad, "oceano", genero, "gris", 6)
        self._listado.append(bacalao)
        Pez.bacalaos += 1
    
    def setListado(self, listado):
        self.__listado = listado
        
    def getListado(self):
        return self.__listado
    
    def setColorEscamas(self, colorEscamas):
        self.__colorEscamas = colorEscamas
        
    def getColorEscamas(self):
        return self.__colorEscamas
    
    def setCantidadAletas(self, cantidadAletas):
        self.__cantidadAletas = cantidadAletas
        
    def getCantidadAletas(self):
        return self.__cantidadAletas  
        
    