# exemplo de composição

from classes import Cliente

print()
cliente1 = Cliente('João', 60)
cliente1.insere_endereco('Belo Horizonte', 'MG')
print(cliente1.nome)
cliente1.lista_enderecos()
print()

# observamos que, ao deletar o cliente 1, seus objetos endereço também são deletados
print('Apagando...')
del cliente1
print()

cliente2 = Cliente('Maria', 50)
cliente2.insere_endereco('Salvador', 'BA')
cliente2.insere_endereco('Rio de Janeiro', 'RJ')
print(cliente2.nome)
cliente2.lista_enderecos()
print()

# o mesmo ocorre com os outros clientes
print('Apagando...')
del cliente2
print()
