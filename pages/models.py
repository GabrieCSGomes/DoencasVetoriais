from django.db import models

# Create your models here.
class fichaVisita(models.Model):

  municipio = models.CharField(
    max_length=255,
    null=False,
    blank=False
  )

  localidade = models.CharField(
    max_length=255,
    null=False,
    blank=False
  )

  quarteirao = models.CharField(
    max_length=255,
    null=False,
    blank=False
  )

  distrito = models.CharField(
    max_length=255,
    null=False,
    blank=False
  )

  rua = models.CharField(
    max_length=255,
    null=False,
    blank=False
  )

  numero = models.IntegerField(
    default=0,
    null=False,
    blank=False
  )