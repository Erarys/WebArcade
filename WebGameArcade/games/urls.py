from django.urls import path
from . import views

app_name = 'games'

urlpatterns = [
    path('', views.index, name='general'),
    path('keyboard/', views.KeyboardRaceView.as_view(), name='keyboard'),
    path('json/', views.my_view, name='json'),
]