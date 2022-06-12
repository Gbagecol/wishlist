from django.http import HttpResponse
from django.shortcuts import render


def indexView(request):
    """
    The index page view.
    """
    return render(request, "wishlist/index.html")


def userView(request, username):
    """
    The view for the user with the given username.
    """
    
    context = {"username": username}

    return render(request, "wishlist/user_home.html", context)