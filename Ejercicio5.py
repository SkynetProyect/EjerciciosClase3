import math


class Circulo:  # se crea la clase circulo
    def __init__(self, radio: float, centro_x: float, centro_y: float):  # se crea el constructor
        self.centro = [centro_x, centro_y]  # se define la posicion del centro
        self.radio = radio  # se define el radio del circulo

    def calcular_area(self):  # se calcula el area con formula Pi*R al cuadrado
        area = math.pi * self.radio ** 2
        return area

    def calcular_perimetro(self):  # se calcula el perimetro con formular 2 pi R
        perimetro = 2 * math.pi * self.radio
        return perimetro

    def punto_en_circulo(self, punto_x: float, punto_y: float):  # funcion para revisar si el punto pertenece al circulo
        # se calcula la distancia del punto dado al centro del circulo
        distancia = ((punto_x - self.centro[0]) ** 2 + (punto_y - self.centro[1]) ** 2) ** (1 / 2)
        if distancia <= self.radio:  # si la distancia es inferior al radio significa que el punto si pertenece al
            # circulo
            return True
        else:
            return False
