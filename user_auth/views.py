from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def new_user(request):
    return render(request, 'auth/new_user.html')

def register_user(request):
    if not request.method == 'POST':
        return HttpResponseNotFound()
    

    body = request.POST
    email = body['username']
    password = body['password']
    first_name = body['first_name']
    last_name = body['last_name']
    if User.objects.filter(email=email):
        request.session['user_exists'] = True
        return redirect('/')

    User.objects.create_user(email=email, username=email, password=password, first_name=first_name, last_name=last_name)
    return redirect('/')

def authenticate_user(request):
    if not request.method == 'POST':
        return HttpResponseNotFound()
    body = request.POST
    username = body['username']
    password = body['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/profile/')
    else:
        new_user(request)
def user_logout(request):

    logout(request)
    return redirect('/')

