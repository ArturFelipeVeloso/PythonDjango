from Produtos import models

def Listar(config):
	models.listarProduto(config)

def Adcionar(config, nome, preco):
	models.addProduto(config, nome, preco)