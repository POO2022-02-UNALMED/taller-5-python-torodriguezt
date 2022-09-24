class Zoologico:
    
    def __init__(self, nombre, ubicacion):
        self.__nombre = nombre
        self.__ubicacion = ubicacion
        self.__zonas = []
        
    def agregarZonas(self, zonas):
        self.__zonas.append(zonas)
    
    
    def cantidadTotalAnimales(self):
        total = 0
        for i in range(0, len(self.__zonas)):
            total = total + self.__zonas[i].cantidadAnimales()
        
    def setNombre(self, nombre):
        self.__nombre = nombre
        
    def getNombre(self):
        return self.__nombre
    
    def setUbicacion(self, ubicacion):
        self.__ubicacion = ubicacion
        
    def getUbicacion(self):
        return self.__ubicacion
    
    def setZonas(self, zonas):
        self.__zonas = zonas
        
    def getZonas(self):
        return self.__zonas