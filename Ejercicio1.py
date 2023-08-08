

class Vehiculo:
    velocidad_maxima: float
    kilometraje: float

    def __init__(self, speed: float = input(), kilo: float = input()):
        self.velocidad_maxima = speed
        self.kilometraje = kilo

    def accesso(self):
        print("La informacion del vehiculo es:  " + str(self.velocidad_maxima) + " MaxSpeed ")
        print(str(self.kilometraje) + " Kilometrake")
