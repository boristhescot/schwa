from django.shortcuts import render, redirect



def userhome(request):
    if request.user.is_authenticated:
        context = {'username': request.user.username}
        return render(request, 'userhome.html', context)
    else:

        return redirect('/')
