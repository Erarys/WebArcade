from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from mailauth.views import PersonalPageView, RegisterView

app_name = 'mailauth'

urlpatterns = [
    path("profile/", PersonalPageView.as_view(), name="personal_page"),
    path(
        "login/",
        LoginView.as_view(
            template_name="mailauth/login.html",
            redirect_authenticated_user=True,
        ),
        name="login",
    ),
    path(
        "logout/",
        LogoutView.as_view(
            template_name="mailauth/login.html"
        ),
        name="logout",
    ),
    path(
        "register/",
        RegisterView.as_view(),
        name="register"
    )
]