from django.shortcuts import render, redirect



def userhome(request):
    if request.user:
        context = {'username': request.user.username}
        return render(request, 'userhome.html', context)
    else:
        redirect('/')
