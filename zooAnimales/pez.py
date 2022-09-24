from zooAnimales.animal import Animal
class Pez(Animal):
    
    salmones = 0
    bacalaos = 0
    listado = []
    
    def __init__(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas):
        super().__init__(nombre, edad, habitat, genero)
        self.__colorEscamas = colorEscamas
        self.__cantidadAletas = cantidadAletas
        Animal.pez += 1
        
    def cantidadPeces(self):
        return len(self.__listado)

    @classmethod
    def crearSalmon(cls, nombre, edad, genero):
        salmon = Pez(nombre, edad, "oceano", genero, "rojo", 6)
        cls.listado.append(salmon)
        Pez.salmones += 1
     
    @classmethod
    def crearBacalao(cls, nombre, edad, genero):
        bacalao = Pez(nombre, edad, "oceano", genero, "gris", 6)
        cls.listado.append(bacalao)
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
        
    