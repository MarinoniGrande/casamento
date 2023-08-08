from django.db import models

# Create your models here.

class Produto(models.Model):
    nome = models.CharField(max_length=200, null=True)
    imagem = models.CharField(max_length=200, null=True)
    preco_cota = models.CharField(max_length=200, null=True)
    qtd_clicks = models.IntegerField(null=True)
    qtd_cotas_maxima = models.IntegerField(null=True)
    preco_total = models.CharField(max_length=200, null=True)
    vlr_preco_total = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    vlr_preco_cota =models.DecimalField(max_digits=12, decimal_places=2, null=True)
    categoria = models.CharField(max_length=200, null=True)


class ProdutoConfirmacao(models.Model):
    produto = models.ForeignKey('Produto', on_delete=models.DO_NOTHING, null=True)
    qtd_cota = models.IntegerField(null=True)
    imagem = models.CharField(max_length=200, null=True)


class ProdutoQRCode(models.Model):
    produto = models.ForeignKey('Produto', on_delete=models.DO_NOTHING, null=True)
    data  = models.CharField(max_length=200, null=True)
    nome  = models.CharField(max_length=200, null=True)


class Confirmacao(models.Model):
    nome  = models.CharField(max_length=200, null=True)
    email  = models.CharField(max_length=200, null=True)
    telefone  = models.CharField(max_length=200, null=True)
    data  = models.CharField(max_length=200, null=True)
    qtd_acompanhantes = models.IntegerField(null=True)
    observacao = models.TextField(null=True)
