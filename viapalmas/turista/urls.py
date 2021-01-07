from django.urls import path
from . import views

app_name = 'tutista'

urlpatterns = [
    path('tu', views.novoTurista, name='tu'),
]