from django.db import models
from django.contrib.auth.models import User


class ProdutoGenerico(models.Model):
	"""
	Aqui é definido por exemplo o produto refrigerante mas não nesta classe nao se define se é coca-cola,
	guarana ou fanta
	"""
	nome = models.CharField(max_length=80,unique=True)
	tipo=models.CharField("Tipo do Produto",max_length=80,unique=True)
	descricao=modelsself.CharField("Descricao do Produto",max_length=120)

	def __unicode__(self):
		return self.nome
	
class ProdutoEspecificacao(models.Model):
	nome = models.CharField(max_length=140,unique=True)
	grupoProduto=models.ForeignKey(ProdutoGenerico,verbose_name="Grupo pertecente")
	valor_de_compra=models.DecimalFields("Valor que produto foi comprado",max_digits=10,decimal_places=2)
	valor_para_venda=models.DecimalFields("Valor para a venda do produto",max_digits=10,decimal_places=2)

	def __unicode__(self):
		return self.nome

class Vendas(models.Model):
	"""
	tabela onde será inserido as transacoes
	"""
	data = models.DateField("data de transacao",auto_now_add=True)
	total = models.DecimalFields("Total da compra",max_digits=10,decimal_places=2)
	