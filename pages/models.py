from django.db import models
from django.urls import reverse

# Create your models here.
class FichaVisita(models.Model): # TABLE Ficha

  distrito = models.ForeignKey('DistritosAdm', on_delete=models.CASCADE)

  endereco = models.ForeignKey('endereco', on_delete=models.CASCADE, verbose_name='Endereço')

  categoria = models.CharField(
    max_length=255,
    blank=False,
    null=False,
  )

  quarto = models.PositiveIntegerField(
      default=0,
      null=False,
      blank=False
    )

  infos = models.ForeignKey('Info', on_delete=models.CASCADE, verbose_name='Informações')

  def get_absolute_url(self):
    return reverse('ficha')

class DistritosAdm(models.Model): #TABLE DA
  
  class bairros(models.IntegerChoices):
    CIDADE_VELHA = 1
    CAMPINA = 2
    REDUTO = 3
    UMARIZAL = 4
    TELEGRAFO = 5
    SACRAMENTA = 6
    PEDREIRA = 7
    MARCO = 8
    SOUZA = 9
    MARAMBAIA = 10
    CANUDOS = 11
    FATIMA = 12
    SAO_BRAS = 13
    NAZARE = 14
    BATISTA_CAMPOS = 15
    JURUNAS = 16
    CONDOR = 17
    GUAMA = 18
    TERRA_FIRME = 19
    CREMACAO = 20
    VAL_DE_CANS = 21
    MIRAMAR = 22
    PRATINHA = 23
    TAPANA = 24
    BENGUI = 25
    MARACANGALHA = 26
    BARREIRO = 27
    UNIVERSITARIO = 28
    CURIO_UTINGA = 29
    AURA = 30
    CASTANHEIRA = 31
    AGUAS_LINDAS = 32
    GUANABARA = 33
    SAO_CLEMENTE = 34
    PARQUE_GUAJARA = 35
    TENONE = 36
    AGUAS_NEGRAS = 37
    MARACACUERA = 38
    PARQUE_VERDE = 39
    CRUZEIRO = 40
    PONTA_GROSSA = 41
    MANGUEIRAO = 42
    CABANAGEM = 43
    CAMPINA_DE_ICOARACI = 44
    PARACURI = 45
    AGULHA = 46
    UNA = 47
    COQUEIRO = 48
    SAO_JAO_DE_OUTEIRO = 49
    ITAITEUA = 50
    AGUAS_NEGRA = 51
    MARACAJA = 52
    VILA = 53
    PRAIA_GRANDE = 54
    FAROL = 55
    MANGUEIRAS = 56
    SAO_FRANCISCO = 57
    CARANANDUBA = 58
    MARAHU = 59
    PARAISO = 60
    BAIA_DO_SOL = 61
    SUCURIJUQUARA = 62
    CARUARA = 63
    BONFIM = 64
    ARIRAMBA = 65
    MURUBIRA = 66
    PORTO_ARTHUR = 67
    NATAL_DO_MORUMBIRA = 68
    CHAPEU_VIRADO = 69
    AEROPORTO = 70

  distritos = [
    ('DAMOS', 'Distrito Administrativos de Mosqueiro'),
    ('DAOUT', 'Distrito Administrativo de Outeiro'),
    ('DAICO', 'Distrito Administrativo de Icoaraci'),
    ('DABEN', 'Distrito Administrativo do Benguí'),
    ('DAENT', 'Distrito Administrativo do Entroncamento'),
    ('DASAC', 'Distrito Administrativo da Sacramenta'),
    ('DABEL', 'Distrito Administrativo de Belém'),
    ('DAGUA', 'Distrito Administrativo de Guamá'),
  ]

  distrito_saude = models.CharField(
    max_length=5,
    choices=distritos,
    null=False,
    blank=False,
    default='DABEL',
    verbose_name='DA'
  )

  bairro = models.IntegerField(
    choices=bairros.choices,
    null=False,
    blank=False,
    default=bairros.CONDOR,
  )

  municipio = models.CharField(
    max_length=255,
    null=False,
    blank=False,
    default='Belém',
    verbose_name='Município'
  )

  def get_absolute_url(self):
    return reverse('distritos')

class Endereco(models.Model): #TABLE Endereco

    rua = models.CharField(
      max_length=255,
      null=False,
      blank=False
    )
  
    complemento = models.CharField(
      max_length=255,
      null=False,
      blank=False
    )

    numero = models.PositiveIntegerField(
      default=0,
      null=False,
      blank=False,
      verbose_name='Número'
    )
    
    unidade_federacao = models.CharField(
      max_length=2,
      null=False,
      blank=False,
      default= 'PA',
      verbose_name='UF'
    )

    def get_absolute_url(self):
      return reverse('endereco')

class Info(models.Model): #TABLE Info
  
    data = models.DateField()
  
    hora = models.TimeField()
  
    atividade = models.CharField(
      max_length=255,
      null=False,
      blank=False
    )

    equipe = models.ForeignKey(
      'equipe',
      on_delete=models.CASCADE,
    )
  
    def get_absolute_url(self):
      return reverse('infos')

class Equipe(models.Model): #TABLE Equipe
  
    nome_agente = models.CharField(
      max_length=255,
      null=False,
      blank=False,
      verbose_name='Nome do Agente'
    )
  
    cargo = models.CharField(
      max_length=255,
      null=False,
      blank=False
    )

    responsavel = models.CharField(
      max_length=255,
      null=False,
      blank=False,
      verbose_name='Responsável'
    )
  
    def get_absolute_url(self):
      return reverse('equipe')