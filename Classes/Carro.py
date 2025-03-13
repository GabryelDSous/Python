class Carro:
    def __init__(self, modelo, cor):
        self.modelo = modelo
        self.cor = cor

    def mostrar_info(self):
        print(f"Modelo: {self.modelo}, Cor: {self.cor}")

carro1 = Carro("Vic","Preto",2, "Ferrari")

carro1.info