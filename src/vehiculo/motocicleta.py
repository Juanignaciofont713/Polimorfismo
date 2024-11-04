from .vehiculo import Vehiculo

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada

    def describir(self):
        return f"{self.tipo_vehiculo()}: {self.marca} {self.modelo}, con {self.cilindrada}cc de cilindrada"

    def tipo_vehiculo(self):
        return "Motocicleta"