from .vehiculo import Vehiculo

class Auto(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas

    def describir(self):
        return f"{self.tipo_vehiculo()}: {self.marca} {self.modelo}, con {self.puertas} puertas"

    def tipo_vehiculo(self):
        return "Automovil"