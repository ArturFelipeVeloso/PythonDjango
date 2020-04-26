from BombomShow import settings, urls
from Produtos import models

meusite = 'www.meusite.com.br'
dbProdutos = models.Produtos()

config = settings.Configuracoes(meusite, dbProdutos)

urls.request(config, 'www.meusite.com.br')

urls.request(config, 'www.meusite.com.br/ADD', 'Arroz', 10.5)

urls.request(config, 'www.meusite.com.br/ADD', 'Feijão', 5.5)

urls.request(config, 'www.meusite.com.br')

urls.request(config, 'www.meusite2.com.br')