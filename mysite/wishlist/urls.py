from . import views
from django.urls import path


#routing for this app
urlpatterns = [
    path("", views.index, name="index") #index
]