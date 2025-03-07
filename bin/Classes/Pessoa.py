class Pessoa: 
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura
    def MostrarInformacoes(self):
        print(f"Nome: {self.nome}\nIdade: {self.idade}\nAltura: {self.altura}")
#* Fim da classe Pessoa

#* Instanciando classes
Pessoa1 = Pessoa("Gabryel", 17, 1.75)
Pessoa2 = Pessoa("Otavio Popo Guloso", 17, 1.89)
Pessoa3 = Pessoa("Matheus Ramesses", 18, 1.90)

ArrayPessoas = [Pessoa1, Pessoa2, Pessoa3]

#* Executando
for pessoa in ArrayPessoas:
    print("---------------------------")
    pessoa.MostrarInformacoes()
# Pessoa1.MostrarInformacoes()