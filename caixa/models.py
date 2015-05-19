# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Produto(models.Model):
	nome = models.CharField(max_length=140,unique=True)
	valor_de_compra=models.DecimalField("Valor que produto foi comprado",max_digits=10,decimal_places=2)
	valor_para_venda=models.DecimalField("Valor para a venda do produto",max_digits=10,decimal_places=2)
	def __unicode__(self):
		return self.nome

class Vendas(models.Model):
	"""
	tabela onde será inserido as transacoes
	"""
	data = models.DateField("data de transacao",auto_now_add=True)
	total = models.DecimalField("Total da compra",max_digits=10,decimal_places=2)
	