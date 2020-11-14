from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):  # This takes in an HttpRequest and all of its meta data. i.e headers
    # Every request must return a response
    return HttpResponse('Hello World!')
