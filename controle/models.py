from django.db import models
from django.contrib.auth.models import User


class Produto(models.Model):
	nome = models.CharField(max_length=80)
	validade = models.DateField()
	tipoProduto=CharField(max_length=80)

"""
	class Meta:
		abstract=True
"""
class TipoProduto(models.Model):
	