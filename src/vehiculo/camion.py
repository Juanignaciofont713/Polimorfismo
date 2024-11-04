from .vehiculo import Vehiculo

class Camion(Vehiculo):
    def __init__(self, marca, modelo, capacidad_carga):
        super().__init__(marca, modelo)
        self.capacidad_carga = capacidad_carga

    def describir(self):
        return f"{self.tipo_vehiculo()}: {self.marca} {self.modelo}, con capacidad de {self.capacidad_carga} toneladas"

    def tipo_vehiculo(self):
        return "Camion"