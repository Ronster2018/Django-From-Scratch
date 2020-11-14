from django.urls import path

from . import views

urlpatterns = [
    # First araguement in the path is the route the URL will take
    # Second is the view to call
    # Third is any name you wish. Allows us to refer to it from anywhere else in the project. More to come in part 2.
    path('', views.index, name='index'),
]
