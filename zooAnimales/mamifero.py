from animal import Animal

class Mamifero(Animal):
    
    caballos = 0
    leones = 0
    
    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        super().__init__(nombre, edad, habitat, genero)
        self.__pelaje = pelaje
        self.__patas = patas
        self._listado = []
        Animal.mamifero += 1
    
    def cantidadMamiferos(self):
        return len(self.__listado)
    
    def crearCaballo(self, nombre, edad, genero):
        caballo = Mamifero(nombre, edad, "pradera", genero, True, 4)
        self._listado.append(caballo)
        Mamifero.caballos += 1

        
    def crearLeon(self, nombre, edad, genero):
        leon = Mamifero(nombre, edad, "selva", genero, True, 4)
        self._listado.append(leon)
        Mamifero.leones += 1
        
        
    def setPelaje(self, pelaje):
        self.__pelaje = pelaje
        
    def getPelaje(self):
        return self.__pelaje
    
    def setPatas(self, patas):
        self.__patas = patas
        
    def getPatas(self):
        return self.__patas