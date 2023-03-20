from django.shortcuts import render, HttpResponse

def send_mail(request):
    return HttpResponse("correo enviado")
