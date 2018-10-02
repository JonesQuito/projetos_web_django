from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Base(models.Model):

    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    descricao = models.TextField(
        null=False,
        blank=False
    )

    atualizacao = models.DateField(
        'Data de atualizacao',
        null=True,
        blank=True
    )

    host = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    owner = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    objetos = models.Manager()
'''
    created_at = models.DateTimeField(
        'Creado em', auto_now_add=True
    ) # auto_now_add ==> preenche com a data apenas no momento da criação

    updated_at = models.DateTimeField(
        'Atualizado em', auto_now=True
    ) # auto_now ==> preenchido sempre que o registro for atulizado
'''
    
