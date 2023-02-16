
# manejo de rutas 
from django.shortcuts import render, redirect
from home import urls

# importe de modelos requeridos 
from home.models import Product
from users.models import Client

# registro y autenticacion de usuarios 
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError

# proteccion de rutas 
from django.contrib.auth.decorators import login_required

# registro
def signup(request):
    if request.method=="GET":
        return render(request,"users/signup.html")
    else:
        # verificamos que las contraseñas coincidan
        if request.POST["password1"] == request.POST["password2"]:
            try:
                # registramos el usuario nuevo 
                user = Client.objects.create_user(
                first_name=request.POST["first_name"],
                last_name=request.POST["last_name"],
                email=request.POST["email"],
                phone=request.POST["phone"],
                username=request.POST["username"], 
                password=request.POST["password1"])
                user.save()
                # le damos un login automantico al usuario
                login(request,user)
                return redirect("users:home")
            # en caso de que el usuario ya este registrado elevamos el error de integridad 
            except IntegrityError: 
                return render(request,"users/signup.html",{
                    "mensaje":"usuario ya existente "
                })
        return render(request,"users/signup.html",{
            "mensaje":"las contraseñas no coinciden "
        })

# autenticacion y login
def signin(request):
    if request.method=="GET":
        return render(request,"users/signin.html")
    else:
        user = authenticate(
            request, 
            username = request.POST["username"], 
            password = request.POST["password"])
        if user == None:
            return render(request,"users/signin.html",{
            "mensaje":" Credenciales incorrectas"
        })
        else:
            login(request,user)
            return redirect("users:home")


@login_required
def home(request, ):
    products = Product.objects.all()
    user=Client.objects.get(pk=request.user.pk) 
    balance=(user.balance)
    balance="{:,.2f}".format(balance)
    return render(request,"users/home.html",{
        "products":products,
        "Client":user,
        "blc":balance
    })


@login_required
def end_sesion(request):
    logout(request)
    return redirect("users:signin")
