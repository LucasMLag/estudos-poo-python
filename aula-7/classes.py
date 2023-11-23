class Escritor:
    def __init__(self, nome):
        self.__nome = nome
        self.__ferramenta = None

    @property
    def nome(self):
        return self.__nome

    @nome.getter
    def nome(self, value):
        self.__nome = value

    @property
    def ferramenta(self):
        return self.__ferramenta

    @ferramenta.getter
    def ferramenta(self, value):
        self.__ferramenta = value


class Caneta:
    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

    @marca.getter
    def marca(self, value):
        self.__marca = value

    def escrever(self):
        print('Caneta está escrevendo...')


class MaquinaDeEscrever:
    def escrever(self):
        print('Maquina está escrevendo...')
