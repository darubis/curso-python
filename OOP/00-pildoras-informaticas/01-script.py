# herencia
class Vehiculos():
    def __init__(self,marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelara = False
        self.frena = False


    def arrancar(self):
        self.enmarcha = True

    def acelerar(self):
        self.acelara = True

    def frena(self):
        self.frena = True

    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.enmarcha, "\nAcelerando: ", self.acelara, "\nFrenando: ", self.frena)


class Furgoneta(Vehiculos):

    def carga(self, cargar):
        self.cargado = cargar
        if (self.cargado):
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta no esta cargada"


# herencia en python
class Moto(Vehiculos):
    hcaballito = ""
    def caballito(self):
        self.hcaballito = "Voy haciendo el caballito"

    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.enmarcha, "\nAcelerando: ", self.acelara, "\nFrenando: ", self.frena, "\n",self.hcaballito)


class VElectricos(Vehiculos):
    def __init__(self):
        super().__init__(marca,modelo)
        self.autonomia = 100

    def cargarEnergia(self):
        self.cargando = True

# Herencia multiple, se da mas preferencia a la clase que esta mas a la izquierda
class BicicletaElectrica(VElectricos,Vehiculos):
    pass


miMoto = Moto("Honda", "CBR")
miMoto.caballito()
miMoto.estado()


print()
miFurgoneta = Furgoneta("Renault","Kangoo")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))


miBici = BicicletaElectrica("Orbea","hj")