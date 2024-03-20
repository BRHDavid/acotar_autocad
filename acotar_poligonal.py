from coordenadas_poligonal import Coordenadas
from pyautocad import APoint as AP

class Acotar(Coordenadas):
    def __init__(self):
        super().__init__()
        self.coordenadas_list= self.coordenadas()
        
    def cotas(self):
        for elemento in self.coordenadas_list:
            puntos = int((len(elemento)-2)/2)
            j = 0      
            for _ in range(puntos):
                punto1 = elemento[j:j+2]
                punto2 = elemento[j+2:j+4]
                
                point_text = AP((punto1[0]+punto2[0])/2 , 
                                (punto1[1]+punto2[1])/2 )

                self.model.AddDimAligned(AP(punto1[0],punto1[1]),
                                    AP(punto2[0],punto2[1]),
                                    point_text)

                j +=2
                
if __name__ == '__main__':
    acotar = Acotar()
    acotar.cotas()
    

