class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def describir(self):
        raise NotImplementedError("Este método debe ser implementado por las clases derivadas")

    def tipo_vehiculo(self):
        return "Vehículo"