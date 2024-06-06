from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse

from .models import Point


def general_page(request: HttpRequest) -> HttpResponse:
    return render(request, 'games/general-page.html')


class KeyboardRaceView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'games/keyboard-race.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        user = request.user
        if not request.user.is_authenticated:
            return HttpResponse("You are not logged in!")
        try:
            data = json.loads(request.body)
            last_record = Point.objects.get(user=user)
            speed = data["speed"]

            if speed > last_record.record:
                last_record.record = speed
                last_record.save()

            response_data = {'message': 'Data received', 'received_data': data}
            return JsonResponse(response_data)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)


class PersonalPageView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'games/personal_page.html')
