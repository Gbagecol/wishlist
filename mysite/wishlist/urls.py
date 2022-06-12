from . import views
from django.urls import path


#routing for this app
urlpatterns = [
    path("", views.indexView, name="index"), #index
    path("user/<str:username>", views.userView, name="user"),
]