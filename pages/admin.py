from django.contrib import admin
from .models import FichaVisita, DistritosAdm, Endereco, Info, Equipe

# Register your models here.
admin.site.register(FichaVisita)
admin.site.register(DistritosAdm)
admin.site.register(Endereco)
admin.site.register(Info)
admin.site.register(Equipe)