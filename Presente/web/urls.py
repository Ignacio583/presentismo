from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listado_personal',views.listado_personal, name='listado_personal')
]