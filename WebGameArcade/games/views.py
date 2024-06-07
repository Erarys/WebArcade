from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, reverse, redirect
from django.views import View
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from django.views.generic import UpdateView

from .models import Point
from mailauth.models import CustomUser


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

    def post(self, request: HttpRequest) -> HttpResponse:
        form = request.POST
        user = CustomUser.objects.get(pk=request.user.pk)
        if form['first_name']:
            user.first_name = form['first_name']
        if form['last_name']:
            user.last_name = form['last_name']
        if form['email']:
            user.email = form['email']
        user.save()
        url = reverse('games:personal_page')
        return redirect(url)