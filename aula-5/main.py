class A:
    # criando uma variável de classe para ser exemplo:
    vdc = 1


# vamos criar duas instâncias, e tentar acessar a variavel atravez delas:

a1 = A()
a2 = A()

print()
print('instânciadas as variáveis:')
print(f'a1.vdc -> {a1.vdc}')
print(f'a2.vdc -> {a2.vdc}')
print()

# modificando a variável de classe para ver o efeito disso nas instâncias existentes:
A.vdc = 2

print('Após o comando "A.vdc = 2":')
print(f'a1.vdc -> {a1.vdc}')
print(f'a2.vdc -> {a2.vdc}')
print()

# tentando modificar a variável de classe da instância a1 apenas:
a1.vdc = 3

print('Após o comando "a1.vdc = 3":')
print(f'a1.vdc -> {a1.vdc}')
print(f'a2.vdc -> {a2.vdc}')
print()

# parece ter funcionado, entretando, acessando o __dict__ das instâncias é possível notar que são diferentes
# a1 agora possui uma variável 'vdc' de instância, e ela é quem está sendo exibida no lugar da variável de classe 'vdc'

print('Observando o __dict__ das duas instâncias e da classe:')
print(f'a1.__dict__: {a1.__dict__}')
print(f'a2.__dict__: {a2.__dict__}')
print(f'A.__dict__: {A.__dict__}')
print()

# quando acessamos uma variével de nome tal através de uma instância
# primeiro o python buscará por uma variável com tal nome que seja da instância em si
# e caso não encontre, então buscará por uma variável com tal nome na classe
