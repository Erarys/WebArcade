from django.urls import path
from .views import (
    general_page,
    KeyboardRaceView,
    PersonalPageView
)

app_name = 'games'

urlpatterns = [
    path('', general_page, name='general'),
    path('keyboard/', KeyboardRaceView.as_view(), name='keyboard'),
    path('profile/', PersonalPageView.as_view(), name='personal_page'),
]