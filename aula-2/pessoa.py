class Pessoa:

    ano_atual = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    # método da classe (não tem parâmetro self, tem parâmetro cls, referente a classe)
    # esse exemplo cria uma nova instância de pessoa, calculando a idade a partir do ano de nascimento
    @classmethod
    def por_ano_de_nascimento(cls, nome, ano_de_nascimento):
        idade = cls.ano_atual - ano_de_nascimento
        return cls(nome, idade)
