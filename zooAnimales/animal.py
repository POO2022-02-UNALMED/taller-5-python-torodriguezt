class Animal:
    
    totalAnimales = 0
    mamifero = 0
    ave = 0
    reptil = 0
    pez = 0
    anfibio = 0
    
    def __init__(self, nombre, edad, habitat, genero):
        self.__nombre = nombre
        self.__edad = edad
        self.__habitat = habitat
        self.__genero = genero
        self.__zona = []
    
    def setNombre(self, nombre):
        self.__nombre = nombre
        
    def getNombre(self):
        return self.__nombre
    
    def setEdad(self, edad):
        self.__edad = edad
        
    def getEdad(self):
        return self.__edad
    
    def setHabitat(self, habitat):
        self.__habitat = habitat
        
    def getHabitat(self):
        return self.__habitat
    
    def setGenero(self, genero):
        self.__genero = genero
    
    def getGenero(self):
        return self.__genero
    
    def toString(self):
        if self.__zona == [] and self.__zona.__getZoo() == None:
            mensaje = f"Mi nombre es {self.__nombre}, tengo una edad de {self.__edad}, habito en {self.__habitat} y mi genero es {self.__genero}"
            return mensaje
        else:
            mensaje = f"Mi nombre es {self.__nombre}, tengo una edad de {self.__edad}, habito en {self.__habitat} y mi genero es {self.__genero} la zona en la que me ubico es {self.__zona} en el {self.__zona[0].__getZoo()}"
            return mensaje
            
    def totalPorTipo():
        mensaje = (f"Mamiferos: {Animal.mamifero}\nAves: {Animal.ave}\nReptiles: {Animal.reptil}\nPeces: {Animal.pez}\nAnfibios: {Animal.anfibio}")
        return mensaje
    
        