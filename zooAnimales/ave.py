from animal import Animal

class Ave(Animal):
    
    halcones = 0
    aguilas = 0
    
    def __init__(self, nombre, edad, habitat, genero, colorPlumas):
        super().__init__(nombre, edad, habitat, genero)
        self.__listado = []
        self.__colorPlumas = colorPlumas
        Animal.ave += 1
        
    def cantidadAves(self):
        return len(self.__listado)
    
    def crearHalcon(self, nombre, edad, genero):
        halcon = Ave(nombre, edad, "montanas", genero,"cafe glorioso")
        self._listado.append(halcon)
        Ave.halcones += 1
    
    def crearAguila(self, nombre, edad, genero):
        aguila = Ave(nombre, edad, "montanas", genero,"blanco y amarillo")
        self._listado.append(aguila)
        Ave.aguilas +=1
    
    def setListado(self, listado):
        self.__listado = listado
        
    def getListado(self):
        return self.__listado
    
    def setColorPlumas(self, colorPlumas):
        self.__colorPlumas = colorPlumas
        
    def getColorPlumas(self):
        return self.__colorPlumas
        
        