from django.shortcuts import render

def main_view(request):
    user_exists = False
    try:
        user_exists = request.session['user_exists']
        del request.session['user_exists']
    except KeyError:
        pass
    context = {
        'user_exists': user_exists
    }
    return render(request, 'main.html', context)
