from django.shortcuts import render

def userhome(request):
    context = {}
    return render(request, 'userhome.html', context)
