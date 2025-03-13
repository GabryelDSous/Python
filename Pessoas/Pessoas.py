class Animal:
    def __init__(self, nome, idade, altura, peso):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
        
    def fazerAno(self):
        self.idade += 1
    
    def mostrarInfo(self):
        print("-="*20)
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Altura: {self.altura}")
        print(f"Peso: {self.peso}")


p1 = Animal("Otavio Nigga", 17, 1.75, 60)
p1.fazerAno()
p1.mostrarInfo()