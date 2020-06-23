from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) # ao excluir o usuário exclui tbm os eventos associados a ele

    class Meta:
        db_table = 'evento'

    # Ao criar o evento será mostrado o título dele no admin
    def __str__(self):
        return self.titulo

