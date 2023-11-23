from random import randint


class Pessoa:

    ano_atual = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # método de instância - recebe a instância como parâmetro (self)
    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    # método de classe - recebe a classe como parâmetro (cls)
    @classmethod
    def por_ano_de_nascimento(cls, nome, ano_de_nascimento):
        idade = cls.ano_atual - ano_de_nascimento
        return cls(nome, idade)

    # método estatico - não recebe nem a instância e nem a classe como parâmetros
    @staticmethod
    def gera_id():
        return randint(10000, 99999)
