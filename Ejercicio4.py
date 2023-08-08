class Rectangulo:
    def __init__(self):
        self.esquina_inferior_izquierda = [0.0, 0.0]
        self.esquina_superior_derecha = [0.0, 0.0]

    def asignar_coordenadas(self, esquina_inferior_x: float, esquina_inferior_y: float, esquina_superior_x: float, esquina_superior_y: float):
        self.esquina_inferior_izquierda[0] = esquina_inferior_x
        self.esquina_inferior_izquierda[1] = esquina_inferior_y
        self.esquina_superior_derecha[0] = esquina_superior_x
        self.esquina_superior_derecha[1] = esquina_superior_y

    