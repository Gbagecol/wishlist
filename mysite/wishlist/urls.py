from . import views
from django.urls import path


#routing for this app
urlpatterns = [
    path("", views.indexView, name="index"), #index
    path("user/<str:username>", views.userView, name="user"),
    path("user/<str:username>/createWishlist", views.createWishlistView, name="new wishlist"),
    path("wishlist/<int:wishlistId>", views.wishlistView, name="wishlist"),
]