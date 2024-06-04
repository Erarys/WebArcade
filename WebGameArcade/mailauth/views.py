from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from mailauth.forms import CustomUserCreationForm


class PersonalPageView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'mailauth/personal_page.html')


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'mailauth/login.html'
    success_url = reverse_lazy("games:general")

    def form_valid(self, form):
        response = super().form_valid(form)

        username = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password1")

        user = authenticate(
            self.request,
            username=username,
            password=password
        )
        login(request=self.request, user=user)

        return response
