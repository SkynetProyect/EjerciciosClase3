class Circulo:
    def __init__(self, radio: float):
        self.centro = []
        self.radio = radio

    def calcular_area(self):
        area = 3.1516 * self.radio ** 2

    def calcular_perimetro(self):
        perimetro = 2*3.1416*self.radio

    def punto_en_circulo(self, punto_x: float, punto_y: float):
        distancia = ((punto_x - self.centro[0]) ** 2 + (punto_y - self.centro[1]) ** 2) ** (1 / 2)
        pertenece = False

        if distancia <= self.radio:
            pertenece = True
        else:
            pass

