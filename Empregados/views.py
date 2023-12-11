from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def register(request):
    if request.method == "GET": 
        return render(request, 'register.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(email=email).first()
        if user:
            return HttpResponse('Usuário já logado')
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        return HttpResponse('usuário cadastrado coom sucesso')



def login (request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(email=email, password=password)

        if user:
            login(request, user)
            return HttpResponse('LOGADO PAIZÃO')
        else:
            return HttpResponse('Email e/ou senha inválidos')


def home (request):
    return HttpResponse("<h1>Página de Home Aqui</h1>")