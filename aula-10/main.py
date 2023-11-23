# já vimos:
# associação -> usa
# agregação -> tem
# composição -> é dono

# nessa aula veremos:
# herança -> é

from classes import *

print()

c1 = Cliente('Carlos', 21)
print(c1.nome)
c1.falar()
c1.comprar()
print()

a1 = Aluno('Joana', 22)
print(a1.nome)
a1.falar()
a1.estudar()
print()

p1 = Pessoa('Marco', 23)
print(p1.nome)
p1.falar()
print()

# vimos que Cliente e Aluno são subclasses que herdam da superclasse Pessoa
