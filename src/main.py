import sys
import os
sys.path.append(os.path.dirname(__file__))

from vehiculo.auto import Auto
from vehiculo.motocicleta import Motocicleta
from vehiculo.camion import Camion
from vehiculo.camioneta import Camioneta


def mostrar_descripciones(vehiculos):
    for vehiculo in vehiculos:
        print(vehiculo.describir())

# Crear una lista de diferentes vehículos
vehiculos = [
    # Autos
    Auto("Toyota", "Corolla", 4), 
    Auto("Honda", "Civic", 4), 
    Auto("Ford", "Mustang", 2), 
    Auto("Chevrolet", "Camaro", 2), 
    Auto("Nissan", "Altima", 4), 
    Auto("Mazda", "3", 4), 
    Auto("Hyundai", "Elantra", 4), 
    Auto("Volkswagen", "Jetta", 4), 
    Auto("BMW", "Serie 3", 4), 
    Auto("Audi", "A4", 4), 
    Auto("Mercedes-Benz", "Clase C", 4), 
    Auto("Kia", "Optima", 4), 
    Auto("Subaru", "Impreza", 4), 
    Auto("Tesla", "Model S", 4), 
    Auto("Volvo", "S60", 4),

    # Motocicletas
    Motocicleta("Yamaha", "MT-07", 689), 
    Motocicleta("Honda", "CBR600RR", 600),
    Motocicleta("Ducati", "Panigale V4", 1103), 
    Motocicleta("Kawasaki", "Ninja H2", 998),
    Motocicleta("BMW", "S1000RR", 999), 
    Motocicleta("Suzuki", "GSX-R750", 750),
    Motocicleta("Harley-Davidson", "Iron 883", 883), 
    Motocicleta("Triumph", "Street Triple", 765),
    Motocicleta("KTM", "Duke 390", 373), 
    Motocicleta("Royal Enfield", "Interceptor 650", 648),
    Motocicleta("Aprilia", "RSV4", 1100), 
    Motocicleta("MV Agusta", "F4", 998),
    Motocicleta("Indian", "FTR 1200", 1203),
    Motocicleta("Benelli", "TNT 600", 600),
    Motocicleta("Husqvarna", "Svartpilen 401", 373),

    # Camiones
    Camion("Volvo", "FH", 25), 
    Camion("Mercedes-Benz", "Actros", 30),
    Camion("Scania", "R500", 40), 
    Camion("MAN", "TGX", 35),
    Camion("Freightliner", "Cascadia", 28), 
    Camion("Kenworth", "W900", 33),
    Camion("Peterbilt", "579", 27), 
    Camion("International", "LT", 29),
    Camion("Mack", "Anthem", 32), 
    Camion("Iveco", "Stralis", 26),
    Camion("DAF", "XF", 31), 
    Camion("Renault", "T Range", 34),
    Camion("Isuzu", "Giga", 20), 
    Camion("Hino", "700", 24), 
    Camion("Foton", "Auman", 22),

    # Camionetas
    Camioneta("Ford", "Ranger", 5), 
    Camioneta("Toyota", "Hilux", 5),
    Camioneta("Chevrolet", "S10", 5),
    Camioneta("Nissan", "Frontier", 5),
    Camioneta("Mitsubishi", "L200", 5), 
    Camioneta("Volkswagen", "Amarok", 5),
    Camioneta("RAM", "1500", 5), 
    Camioneta("Honda", "Ridgeline", 5),
    Camioneta("GMC", "Canyon", 5), 
    Camioneta("Jeep", "Gladiator", 5),
    Camioneta("Mazda", "BT-50", 5), 
    Camioneta("SsangYong", "Musso", 5),
    Camioneta("Great Wall", "Poer", 5), 
    Camioneta("JAC", "T8", 5), 
    Camioneta("Fiat", "Toro", 5)
]

# Llamada a la función polimórfica
mostrar_descripciones(vehiculos)
