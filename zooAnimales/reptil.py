from zooAnimales.animal import Animal
    
class Reptil(Animal):
    
    iguanas = 0
    serpientes = 0
    __listado = []
    
    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola):
        super().__init__(nombre, edad, habitat, genero)
        self.__colorEscamas = colorEscamas
        self.__largoCola = largoCola
        Animal.reptil += 1
        
    @classmethod
    def cantidadReptiles(cls):
        return len(cls.__listado)
    
    @classmethod
    def crearIguana(cls, nombre, edad, genero):
        iguana = Reptil(nombre, edad, "humedal", genero,"verde", 3)
        cls.__listado.append(iguana)
        cls.iguanas += 1
    
    @classmethod
    def crearSerpiente(cls, nombre, edad, genero):
        serpiente = Reptil(nombre, edad, "jungla", genero,"blanco", 1)
        cls.__listado.append(serpiente)
        cls.serpientes += 1
    
    def setListado(self, listado):
        self.__listado = listado
        
    def getListado(self):
        return self.__listado
    
    def setColorEscamas(self, colorEscamas):
        self.__colorEscamas = colorEscamas
        
    def getColorEscamas(self):
        return self.__colorEscamas
    
    def setLargoCola(self, largoCola):
        self.__largoCola = largoCola
        
    def getLargoCola(self):
        return self.__largoCola
    
