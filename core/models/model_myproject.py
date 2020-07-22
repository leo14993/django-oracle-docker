from django.db import models
import datetime

class MyProject(models.Model):
    index_bd = models.IntegerField('index_bd', primary_key=True, db_index=True, blank=True)
    cor = models.CharField('cor', blank=True, max_length=10)
    valor = models.FloatField('valor', blank=True, default=0)
    data_hora = models.DateTimeField('data_hora',  blank=False)
    class Meta:
        db_table = 'Tabela_MyProject'
        unique_together = ['cor', 'data_hora']

# unique_together deixa as duas colunas da tabela como se fossem unicas juntas, 
# ex: não é possível inserir uma cor com as mesma data