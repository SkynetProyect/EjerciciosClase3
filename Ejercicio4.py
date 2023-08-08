from Ejercicio2 import Punto


class Rectangulo:  # crea la clase rectangulo
    def __init__(self):
        self.esquina_izquierda = Punto(0.0, 0.0)  # se le asigna dos instancias de tipo Punto
        self.esquina_derecha = Punto(0.0, 0.0)

    def perimetro(self):  # formula para calcular el perimetro
        largo_en_x = abs(self.esquina_izquierda.posicion_X - self.esquina_derecha.posicion_X)
        largo_en_y = abs(self.esquina_izquierda.posicion_y - self.esquina_derecha.posicion_y)
        return 2 * largo_en_x + 2 * largo_en_y  # retorna el resultado de la formula del perimetro

    def area(self):  # formula para calcular el area
        area = abs(self.esquina_izquierda.posicion_X - self.esquina_derecha.posicion_X) \
               * abs(self.esquina_izquierda.posicion_y - self.esquina_derecha.posicion_y)
        return area # retorna el area

    def es_cuadrado(self):  # formula para saber si es cuadrado
        if abs(self.esquina_izquierda.posicion_X - self.esquina_derecha.posicion_X) == \
                abs(self.esquina_izquierda.posicion_y - self.esquina_derecha.posicion_y):
            return True  # retorna true si es un cuadrado
        else:
            return False  # retorna false si no es un cuadrado
