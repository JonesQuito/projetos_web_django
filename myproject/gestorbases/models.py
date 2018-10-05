from django.db import models
from django.utils.translation import ugettext_lazy as _


class Base(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    atualizacao = models.DateField('Data de atualizacao', null=True, blank=True)
    host = models.CharField(max_length=255, null=False, blank=False)
    owner = models.CharField(max_length=255, null=False, blank=False)
    objetos = models.Manager()

    def __str__(self):
        return self.nome


class Tabela(models.Model):
    base = models.ForeignKey(Base, on_delete=models.CASCADE)
    #base = models.ForeignKey(Base, on_delete=models.CASCADE, choices = bases)
    nome = models.CharField(max_length=255, null=True, blank=True)
    descricao = models.TextField(max_length=255, null=True, blank=True)
    esquema = models.CharField(max_length=255, null=True, blank=False)
    objetos = models.Manager()

    def __str__(self):
        return self.nome
     


class Atualizacao(models.Model):
    tabela = models.ForeignKey(Tabela, on_delete=models.CASCADE)
    data_atualizacao = models.DateField('Data da atualizacao', auto_now_add=True)
    responsavel = models.CharField(max_length=255, null=False, blank=False)
    observacoes = models.TextField(null=True, blank=True)
    mes_ref = models.IntegerField(null=True, blank=True)
    ano_ref = models.IntegerField(null=True, blank=True)
    origem_dados = models.CharField(max_length=255, null=False, blank=False)
    objetos = models.Manager()

        

'''
    created_at = models.DateTimeField(
        'Creado em', auto_now_add=True
    ) # auto_now_add ==> preenche com a data apenas no momento da criação

    updated_at = models.DateTimeField(
        'Atualizado em', auto_now=True
    ) # auto_now ==> preenchido sempre que o registro for atulizado
'''
    
