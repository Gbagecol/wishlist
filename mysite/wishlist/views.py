from .models import User, Wishlist
from django.http import HttpResponse
from django.shortcuts import redirect, render


def indexView(request):
    """
    The index page view.
    """
    return render(request, "wishlist/index.html")

def userView(request, username):
    """
    The view for the user with the given username.
    """
    
    wishlists = [wl for wl in Wishlist.objects.filter(owner_id=username)] #retrieve all wishlists owned by user

    context = {
        "username": username,
        "wishlistList": wishlists
    }

    return render(request, "wishlist/user_home.html", context)

def createWishlistView(request, username):
    """
    Creates a new wishlist in the database for the current user and redirects the user to the existing wishlist page.
    """

    currentUser = User.objects.get(username=username) #get object for current user
    newWishlist = currentUser.wishlist_set.create() #create wishlist and add to user's list

    return redirect("/wishlist/wishlist/{}".format(newWishlist.id))

def wishlistView(request, wishlistId):
    """
    The view for an existing wishlist.
    """

    return HttpResponse("viewing wishlist {}".format(wishlistId))