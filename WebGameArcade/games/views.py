from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View


def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'games/general-page.html')


class KeyboardRaceView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'games/keyboard-race.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        print(request.POST)
        return HttpResponse(f"{request.POST}")


class JsonTestView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'games/json-test.html')