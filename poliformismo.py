class Vehiculo:
    def mover(self):
        pass

class Coche(Vehiculo):

    def sonido(self):
        print("El carro hace vruuuum vruuuuuuuuuuuuuuuuuuuuuum")

    def mover(self):
        print("El carro se está moviendo.")

class Bicicleta(Vehiculo):
    def mover(self):
        print("La bicicleta está pedaleando.")

def mover_vehiculo(vehiculo):
    vehiculo.mover()

coche = Coche()
bicicleta = Bicicleta()

mover_vehiculo(coche)
mover_vehiculo(bicicleta)

