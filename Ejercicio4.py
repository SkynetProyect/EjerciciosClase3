from Ejercicio2 import Punto


class Rectangulo:
    def __init__(self):
        self.esquina_izquierda = Punto(0.0, 0.0)
        self.esquina_derecha = Punto(0.0, 0.0)

    def perimetro(self):
        largo_en_x = abs(self.esquina_izquierda.posicion_X - self.esquina_derecha.posicion_X)
        largo_en_y = abs(self.esquina_izquierda.posicion_y - self.esquina_derecha.posicion_y)
        return 2 * largo_en_x + 2 * largo_en_y

    def area(self):
        area = abs(self.esquina_izquierda.posicion_X - self.esquina_derecha.posicion_X) \
               * abs(self.esquina_izquierda.posicion_y - self.esquina_derecha.posicion_y)
        return area

    def es_cuadrado(self):
        if abs(self.esquina_izquierda.posicion_X - self.esquina_derecha.posicion_X) == \
                abs(self.esquina_izquierda.posicion_y - self.esquina_derecha.posicion_y):
            return True
        else:
            return False
