from django.urls import path
from .views import FichaDeleteView, FichaListView, FichaCreateView, FichaUpdateView, HomePageView, FichaDetailView, InfoCreateView, InfoDeleteView, InfoUpdateView

urlpatterns = [
    path('ficha/lista/', FichaListView.as_view(), name='ficha_list'),
    path('ficha/<int:pk>/editar/', FichaUpdateView.as_view(), name='ficha_update'),
    path('ficha/<int:pk>/deletar/', FichaDeleteView.as_view(), name='ficha_delete'),
    path('', HomePageView.as_view(), name='home'),
    path('ficha/cadastro/', FichaCreateView.as_view(), name='ficha_create'),
    path('ficha/<int:pk>/detalhes/', FichaDetailView.as_view(), name='ficha_read'),
    path('ficha/<int:idf>/info/<int:pk>/deletar', InfoDeleteView.as_view(), name='info_delete'),
    path('ficha/<int:idf>/info/<int:pk>/editar', InfoUpdateView.as_view(), name='info_update'),
    path('ficha/<int:pk>/info/cadastro', InfoCreateView.as_view(), name='info_create'),
]