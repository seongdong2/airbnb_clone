from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("login", views.LoginView.as_view(), name="login"),
    path("login/github", views.github_login, name="github-login"),
    path("login/github/callback", views.github_callback, name="github-callback"),
    path("login/kakao", views.kakao_login, name="KAKAO-login"),
    path("logout", views.log_out, name="logout"),
    path("signup", views.SignUPView.as_view(), name="signup"),
    path("verify/<str:key>", views.complete_verification, name="complete-verification"),
]
