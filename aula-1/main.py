# importa a classe Pessoa do arquivo pessoa.py no mesmo diretório
# foi nescessário criar um arquivo __init__.py vazio no diretório para que o import funcionasse
from pessoa import Pessoa

# criação de instancias, cada uma com seus diferentes atributos
p1 = Pessoa('Luiz', 25)
p2 = Pessoa('João', 23)

# chamada de métodos para testes
# é interessante notar que eles são independentes entre as diferentes instancias
p1.falar('POO')
p2.falar('filmes')
p1.parar_de_falar()
p1.comer()
