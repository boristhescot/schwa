from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from django.contrib.auth.models import User

# Create your views here.
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
    User.objects.create_user(email=email, username=email, password=password, first_name=first_name, last_name=last_name)
    return redirect('/')