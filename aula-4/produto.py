class Produto:
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    def desconto(self, percentual):
        self._preco = self._preco - (self._preco * (percentual / 100))

    # getter
    @property
    def preco(self):
        print(f'O preço foi acessado via getter! Valor atual: {self._preco}')
        return self._preco

    # setter
    @preco.setter
    # esse 'value: float' apenas indica o tipo de entrada esperada, mas não faz restrições
    def preco(self, value: float):
        # exemplo de validação:
        # 1. checa se 'value' é int, e se for, transforma ele em float
        if isinstance(value, int):
            value = float(value)
        # 2. checa se 'value' ainda não é float, e se não for,
        if not isinstance(value, float):
            raise TypeError

        self._preco = value
        print(f'O preço foi alterado via setter! Valor mudado para: {
              self._preco}')

    # deleter
    @preco.deleter
    def preco(self):
        del self._preco
        print(f'O preço foi deletado via deleter!')
