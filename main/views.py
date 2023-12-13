from django.shortcuts import render, redirect

def main_view(request):
    user_exists = False
    if request.user.is_authenticated:
        return redirect('/profile/')
    try:
        user_exists = request.session['user_exists']
        del request.session['user_exists']
    except KeyError:
        pass
    context = {
        'user_exists': user_exists
    }
    return render(request, 'main.html', context)
