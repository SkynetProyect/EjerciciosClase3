

class Punto:  # crea la clase de tipo punto

    def __init__(self, posicion_x: float, posicion_y: float):  # define el constructor con entradas
        # de usuario de tipo float
        self.distancia = None
        self.posicion_X = posicion_x  # asigna la coordenada X en la posicion 1 del array
        self.posicion_y = posicion_y  # asigna la coordenada Y en la posicion 2 del array

    def mostrar(self):  # hecho para devolver las coordenadas ingresadas
        print("Coordenadas ingresadas: " + str(self.posicion_X))  # retorna la coordenada ingresada por el usuario

    def mover(self, entrada1: float = input(), entrada2: float = input()):  # hecho para cambiar las coordenadas
        self.posicion_X = entrada1  # asigna la coordenada X en la posicion 1 del array
        self.posicion_y = entrada2  # asigna la coordenada Y en la posicion 2 del array

    def calcular_distancia(self, punto_x: float, punto_y: float):
        """calcula la distancia entre el punto actual y otro
         punto"""

        # aplica la formula para calcular la distancia

        self.distancia: float = ((punto_x - self.posicion_X)**2 + (punto_y - self.posicion_y)**2)**(1/2)
        return self.distancia  # se retorna la distancia
