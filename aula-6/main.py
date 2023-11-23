'''
encapsulamento em outras linguagens como C ou Java é feito por modificadores de acesso da propria linguagem como:
-> public, protected, private
mas esses modificadores não são usados pensando na segurança do código
existem brechas de segurança e truques para poder burlar esses modificadores

encapsulamento em python é feito através de uma convensao de nomes de atributos e metodos
atributo ou metodo -> public
_atributo ou _metodo -> protected
__atributo ou __metodo -> private

nenhum deles é muito forte em python, como tentam ser nas outras linguagens
já que python espera que os devs saibam o que estão fazendo -- "we're all consenting adults"
atributos protected não tem nenhuma diferença em relaçao a atributos publicos, apenas a diferença de nome
e atributos private ainda são possiveis de se acessar de fora do metodo utilizando um nome diferente especifico
ex.: 'instancia.__atributo' não daria certo, mas 'instancia._classe__atributo' funcionaria normalmente

eles não tem funções reais de segurança, e servem mais como estimulos para boas praticas como o uso de getters e setters
e de uma maneira geral eles são usados para que os proprios devs saibam que não deveriam acessar tais coisas diretamente
'''


class Pessoa:

    def __init__(self, name, age, gender):

        # exemplos de atributos "privados"
        self.__nome = name
        self.__age = age
        self.__gender = gender

    @property
    def nome(self):
        print('Getter Ativado! :]')
        return self.__nome

    @nome.setter
    def nome(self, value):
        if isinstance(value, str):
            print('Setter Ativado! :]')
            self.__nome = value


# criando uma estancia para usar de exemplo
p1 = Pessoa('Luiz', 20, 'h')
print(f'Estância criada com nome {p1.nome}, e nome recebido pelo getter!')
print()

# mudando o nome dela atravez do setter
p1.nome = "João"
print(f'Nome validado e alterado pelo setter para {p1.nome}, e nome recebido pelo getter!')
print()

# "burlando o sistema":
# apesar do atributo __nome ser privado, ele ainda pode ser acessado de fora da classe
p1._Pessoa__nome = 1234
print(f'Nome alterado sem setter, e exibido sem getter: "{p1._Pessoa__nome}"! :[')
print()
