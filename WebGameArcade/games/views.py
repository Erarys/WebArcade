from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, reverse, redirect
from django.http import JsonResponse
from django.views import View

from mailauth.forms import CustomUserUpdateForm
from mailauth.models import CustomUser
from .models import Point
import json


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
        if request.user.is_authenticated:
            context = {
                "form": CustomUserUpdateForm(instance=request.user),
                "points": Point.objects.select_related("user").order_by('-record')[:5]
            }
            return render(request, 'games/personal_page.html', context=context)
        return render(request, 'games/personal_page.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        form = CustomUserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            url = reverse('games:personal_page')
            return redirect(url)
        return render(request, 'games/personal_page.html', context={'form': form})


class AboutWebsiteView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'games/about_website.html')


class ProjectsView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'games/projects.html')
