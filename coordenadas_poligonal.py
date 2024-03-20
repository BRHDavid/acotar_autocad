from inicializador import Inicializador
from grupo_seleccion import Seleccion

class Coordenadas(Inicializador, Seleccion ):
    def __init__(self):
        Inicializador.__init__(self)
        Seleccion.__init__(self)
        self.coordenadas_list = []
        
    def coordenadas(self)-> list:
        
        for elemento in self.grupo:
            self.coordenadas_list.append(elemento.Coordinates)
            
        return self.coordenadas_list
    
if __name__ == '__main__':
    valor = Coordenadas()
    print(valor.coordenadas())

