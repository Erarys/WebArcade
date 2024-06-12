from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, reverse
from django.views import View
from django.views.generic import CreateView

from mailauth.forms import CustomUserCreationForm
from games.models import Point


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'mailauth/login.html'
    success_url = reverse_lazy("games:general")

    def form_valid(self, form):
        response = super().form_valid(form)

        Point.objects.create(user=self.object)

        username = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password1")

        user = authenticate(
            self.request,
            username=username,
            password=password
        )
        login(request=self.request, user=user)

        return response

class LogoutView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        logout(request)
        url = reverse('mailauth:login')
        return redirect(url)
