from django.urls import path
from .views import IndexView, SalaView, SobreView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('chat/<str:nome_sala>/', SalaView.as_view(), name='sala'),
    path('about', SobreView.as_view(), name='about'),
]