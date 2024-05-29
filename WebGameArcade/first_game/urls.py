from django.urls import path
from . import views

app_name = 'first_game'

urlpatterns = [
    path('', views.keyboard_race, name='keyboard')
]