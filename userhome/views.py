from django.shortcuts import render

def userhome(request):
    context = {'username': request.user.username}
    return render(request, 'userhome.html', context)
