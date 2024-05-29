from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def keyboard_race(request: HttpRequest):
    return render(request, 'first_game/keyboard-race.html')
