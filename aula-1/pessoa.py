class Pessoa:
    # exemplo de variavel da classe
    # é valida para todas instancias, e ainda requer o uso de 'self.' para ser acessada pelos metodos
    ano_atual = 2023  # poderia ser melhor implementada utilizando a biblioteca datetime

    # "construtor" python: __init__
    # é chamado sempre que uma instância for criada
    def __init__(self, nome, idade, comendo=False, falando=False):

        # self aqui representa a instância criada, e é passado automaticamente como parametro
        # ex.: em "p1 = Pessoa(nome, idade)" p1 seria self

        # isso está alocando os parâmetros como variáveis da instância:
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

        # os parâmetros "comendo" e "falando" tem valor padrão na classe
        # e então não é nescessario que sejam passados como parâmetros

    # método falar:
    # não acontecera nada se a pessoa já estiver falando ou comendo
    # se a pessoa estiver disponivel, ela começara a falar sobre o assunto recebido como parametro
    def falar(self, assunto):

        # primeiro checamos se a pessoa está disponivel para falar:

        # 1. checa se a pessoa está comendo, e se estiver, retorna com uma mensagem de erro
        if self.comendo:
            print(f'{self.nome} não pode falar comendo.')
            return

        # 2. checa se a pessoa está falando, e se estiver, retorna com uma mensagem de erro
        if self.falando:
            print(f'{self.nome} já esta falando.')
            return

        # não é nescessario 'else' aqui, pois os 'if' anteriores terminavam com 'return'
        # pessoas que não estão disponiveis para falar não chegam a esse ponto do código

        # realiza o objetivo do metodo, fazendo a pessoa falar, e mostra uma mensagem na tela:
        self.falando = True
        print(f'{self.nome} está falando sobre {assunto}.')

    # abaixo há outros métodos muito parecidos com o método falar, mas sem anotações

    # metodo parar_de_falar:
    def parar_de_falar(self):
        if not self.falando:
            print(f'{self.nome} não esta falando.')
            return

        self.falando = False
        print(f'{self.nome} parou de falar.')

    # metodo comer:
    def comer(self, alimento):
        if self.falando:
            print(f'{self.nome} não pode comer falando.')
            return

        if self.comendo:
            print(f'{self.nome} já está comendo.')
            return

        self.comendo = True
        print(f'{self.nome} está comendo {alimento}.')

    # metodo parar_de_comerr:
    def parar_de_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return

        self.comendo = False
        print(f'{self.nome} parou de comer.')

    # exemplo usando a variavel da classe
    # não é muito preciso, podendo ter até 1 ano de erro por não considerar meses, dias, horas, etc
    def get_ano_nascimento(self):
        return self.ano_atual - self.idade
