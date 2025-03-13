class ModeloCarro:
    def __init__(self, nomeCarro, tipo, corCarro, marcaCarro, qtdPortas):
        self.nomeCarro = nomeCarro
        self.tipo = tipo
        self.corCarro = corCarro
        self.marcaCarro = marcaCarro
        self.qtdPortas = qtdPortas
        
        if tipo == 1: self.maxVel = 100
        elif tipo == 2: self.maxVel = 160
        elif tipo == 3: self.maxVel = 200
        elif tipo == 4: self.maxVel = 300
        else: self.maxVel = 80
        
    def mostrarInfo(self):
        print("="*20)
        print(f"Nome: {self.nomeCarro}")
        print(f"Velocidade maxima: {self.maxVel}")
        print(f"Cor: {self.corCarro}")
        print(f"Marca: {self.marcaCarro}")
        print(f"Quantidade de portas: {self.qtdPortas}")
        
class CarroFuturo(ModeloCarro):
    def __init__(self, nomeCarro, tipo, corCarro, marcaCarro, qtdPortas):
        super().__init__(nomeCarro, tipo, corCarro, marcaCarro, qtdPortas)
        if tipo == 1: self.maxVel = 400
        elif tipo == 2: self.maxVel = 650
        elif tipo == 3: self.maxVel = 900
        elif tipo == 4: self.maxVel = 1000
        else: self.maxVel = 280
    
    def mostrarInfo(self):
        super().mostrarInfo()
        print("====== FUTURO ======")
        print("Seu carro pode voar")
        print("Seu carro pode teletransportar")
        print("Seu carro pode alterar a cor")

# Carros normais
carroNomel01 = ModeloCarro("Rapidão", 3, "Blue", "Audi", 2)
carroNomel02 = ModeloCarro("King", 1, "Vermelho", "Lua", 4)
# Carros futuro
carrofuturo01 = CarroFuturo("Javeiro", 4, "Marron", "Futuro", 2)

carroNomel01.mostrarInfo()
carroNomel02.mostrarInfo()
carrofuturo01.mostrarInfo()
print("="*20)
# carroNomela01 = ModeloCarro("Rapidão", 3, "Blue", "Audi", 2)
