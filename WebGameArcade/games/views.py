from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'games/index.html')


def keyboard_race(request: HttpRequest):
    return render(request, 'games/keyboard-race.html')
