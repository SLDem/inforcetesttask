from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="authentication/login.html"),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(next_page="index"), name="logout"),
    path("signup/", views.signup, name="signup"),
    path("employees/", views.EmployeeList.as_view()),
]
