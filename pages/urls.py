from django.urls import path
from .views import FormFichaVisita, HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('ficha/',FormFichaVisita.as_view(), name='ficha')
]