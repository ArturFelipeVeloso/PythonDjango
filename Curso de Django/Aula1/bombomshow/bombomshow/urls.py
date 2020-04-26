from Produtos import views

def request(config, endereco='', produto='', preco=''):
	if endereco == config.site:
		views.Listar(config)
	elif endereco == f'{config.site}/ADD':
		views.Adcionar(config, produto, preco)
	else:
		print('Requisição errada! 404!')