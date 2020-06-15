from django.db import models

# Create your models here.


class Soja(models.Model):
    data = models.DateField('Data')
    cotacao = models.FloatField('Cotação')
    variacao = models.FloatField('Variação')


class Milho(models.Model):
    data = models.DateField('Data')
    cotacao = models.FloatField('Cotação')
    variacao = models.FloatField('Variação')


CAFE_CHOICES = [('Arabica', 'Arabica'), ('Conillon', 'Conillon')]


class Cafe(models.Model):
    tipo = models.CharField('Tipo', choices=CAFE_CHOICES,
                            default='Arabica', max_length=10)
    data = models.DateField('Data')
    cotacao = models.FloatField('Cotação')
    variacao = models.FloatField('Variação')
