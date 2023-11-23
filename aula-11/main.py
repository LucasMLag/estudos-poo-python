from person import Person
from personv2 import PersonV2

john1 = Person('John', 'Doe')
john2 = Person('John', 'Doe')
mary = Person('Mary', 'Jane')
print(john1)
print(repr(john1))
print(john1 == john2)
print()

john1 = PersonV2('John', 'Doe')
john2 = PersonV2('John', 'Doe')
mary = PersonV2('Mary', 'Jane')
print(john1)
print(repr(john1))
print(john1 == john2)
print()

# dataclasses ajudam a escrever menos código, e atingir uma funcionalidade parecida
# usadas para classes de gerenciamento de dados