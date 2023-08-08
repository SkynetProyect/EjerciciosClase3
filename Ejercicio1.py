class Vehiculo:  # clase vehiculo creada

    def __init__(self, speed: float, kilo: float):  # constructor creado, variables definidas
        self.velocidad_maxima = speed  # variable velocidad maxima asignada
        self.kilometraje = kilo  # variable kilometraje asignada

    def accesso(self):  # funcion para leer la informacion guardada
        print("La informacion del vehiculo es:  " + str(self.velocidad_maxima) + " MaxSpeed ")
        print(str(self.kilometraje) + " Kilometrake")
