from django.shortcuts import render


def home(request):
    """ Home page """
    context = {}
    return render(request, 'landing/home.html', context)
