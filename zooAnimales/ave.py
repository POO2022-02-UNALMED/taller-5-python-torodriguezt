from zooAnimales.animal import Animal

class Ave(Animal):
    
    halcones = 0
    aguilas = 0
    __listado = []
    
    def __init__(self, nombre, edad, habitat, genero, colorPlumas):
        super().__init__(nombre, edad, habitat, genero)
        self.__colorPlumas = colorPlumas
        Animal.ave += 1
        
    @classmethod
    def cantidadAves(cls):
        return len(cls.__listado)
    
    @classmethod
    def crearHalcon(cls, nombre, edad, genero):
        halcon = Ave(nombre, edad, "montanas", genero,"cafe glorioso")
        cls.__listado.append(halcon)
        cls.halcones += 1
    
    @classmethod
    def crearAguila(cls, nombre, edad, genero):
        aguila = Ave(nombre, edad, "montanas", genero,"blanco y amarillo")
        cls.__listado.append(aguila)
        cls.aguilas +=1
    
    def setListado(self, listado):
        self.__listado = listado
        
    def getListado(self):
        return self.__listado
    
    def setColorPlumas(self, colorPlumas):
        self.__colorPlumas = colorPlumas
        
    def getColorPlumas(self):
        return self.__colorPlumas
    
        