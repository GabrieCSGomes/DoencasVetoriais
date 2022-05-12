from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from pages.forms import InsereFichaVisita
from pages.models import fichaVisita

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class FormFichaVisita(CreateView):
    template_name = 'ficha.html'
    model = fichaVisita
    form_class = InsereFichaVisita