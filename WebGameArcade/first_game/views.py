from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def main(request: HttpRequest):
    return render(request, 'first_game/base.html')
