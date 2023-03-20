from django.urls import path
from . import views

app_name="fact"

urlpatterns = [
   path("send_mail", views.send_mail, name="send_mail")
]