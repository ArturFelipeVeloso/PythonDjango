class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class Produtos:
    def __init__(self):
        self.produtos = []

    def addProduto(self, Produto):
        self.produtos.append(Produto)

    def listarProdutos(self):
        print('Produtos:')
        for produto in self.produtos:
            print(f'-- Produto: {produto.nome}, Preço: {produto.preco}')

def listarProduto(config):
    config.bd.listarProdutos()

def addProduto(config, nome, preco):
    ProdutoNovo = Produto(nome, preco)
    config.bd.addProduto(ProdutoNovo)
    print(f'O produto {nome} foi adicionado com sucesso!')