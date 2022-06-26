from django.urls import path
from .views import FichaDeleteView, FichaListView, FichaCreateView, FichaUpdateView, HomePageView, FichaDetailView

urlpatterns = [
    path('ficha/lista/', FichaListView.as_view(), name='ficha_list'),
    path('ficha/<int:pk>/editar/', FichaUpdateView.as_view(), name='ficha_update'),
    path('ficha/<int:pk>/deletar/', FichaDeleteView.as_view(), name='ficha_delete'),
    path('', HomePageView.as_view(), name='home'),
    path('ficha/cadastro/', FichaCreateView.as_view(), name='ficha_create'),
    path('ficha/<int:pk>/detalhes/', FichaDetailView.as_view(), name='ficha_read'),
]