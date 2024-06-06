from django.urls import path
from . import views

app_name = 'games'

urlpatterns = [
    path('', views.general_page, name='general'),
    path('keyboard/', views.KeyboardRaceView.as_view(), name='keyboard'),
]