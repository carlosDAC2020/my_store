from django.urls import path
from . import views

app_name="users"

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("signin/", views.signin, name="signin"),
    path("logout/", views.end_sesion, name="logout"),
    path("home/", views.home, name="home")
]