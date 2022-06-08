from django.urls import path
from .views import FichaRegistroView, HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('ficha/', FichaRegistroView.as_view(), name='ficha'),
    #path('ficha/<int:pk>/', FichaDetailView.as_view(), name='ficha_detail')
]