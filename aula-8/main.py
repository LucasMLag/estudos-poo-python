from classes import CarrinhoDeCompras, Produto

carrinho = CarrinhoDeCompras()
p1 = Produto('Camiseta', 40.00)
p2 = Produto('Calça', 80.00)
p3 = Produto('Meia', 10.00)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p1)

carrinho.lista_produtos()

print(f'total: {carrinho.soma_total()}')
