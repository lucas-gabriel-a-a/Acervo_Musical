from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = 'index'),
    path('artista/<int:id_artista>',views.ver_artista,name='ver_artista')
]

