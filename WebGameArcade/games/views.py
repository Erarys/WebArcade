from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse


def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'games/general-page.html')


class KeyboardRaceView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'games/keyboard-race.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        try:
            data = json.loads(request.body)
            print(data)  # Печатает JSON-данные в консоль
            response_data = {'message': 'Data received', 'received_data': data}
            # return render(request, 'games/keyboard-race.html')

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)


def my_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print(data)  # Печатает JSON-данные в консоль
            response_data = {'message': 'Data received', 'received_data': data}
            return JsonResponse(response_data)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    return render(request, 'games/json-test.html')
