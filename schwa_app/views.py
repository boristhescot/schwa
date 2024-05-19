from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def schwa_home(request):
    if request.user.is_authenticated:
        context = {'username': request.user.username}
        return render(request, 'schwa_home.html', context=context)
    else:

        return redirect('/')