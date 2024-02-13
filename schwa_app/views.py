from django.shortcuts import render

def schwa_home(request):
    return render(request, 'schwa_home.html')
