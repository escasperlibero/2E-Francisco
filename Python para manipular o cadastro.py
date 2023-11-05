class AnimalEstimacao:
    def __init__(self):
       .nome = ""
        self.raca = ""
        self.idade = 0
        self.responsavel = ""
        self.telefone = ""

    def cadastrar_animal_estimacao(self):
        self.nome = input("Nome do animal: ")
        self.raca = input("Raça do animal: ")
        self.idade = int(input("Idade do animal: "))
        self.responsavel = input("Nome do responsável: ")
        self.telefone = input("Telefone do responsável: ")

    def retornar_cadastro_animal_estimacao(self):
        cadastro = "Nome: {}
Raça: {}
Idade: {}
Responsável: {}
Telefone: {}".format(
            self.nome, self.raca, self.idade, self.responsavel, self.telefone)
        
        return cadastro


# Exemplo de uso:
animal = AnimalEstimacao()
animal.cadastrar_animal_estimacao()
cadastro_animal = animal.retornar_cadastro_animal_estimacao()
print(cadastro_animal)