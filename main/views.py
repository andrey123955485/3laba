import requests
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


def home_page(request: HttpRequest) -> HttpResponse:
    url = "https://dog.ceo/api/breeds/image/random/10"
    response = requests.get(url)
    data = response.json()
    images = data['message']
    return render(request, 'main/gallery.html', {'images': images})

def about(request: HttpRequest) -> HttpResponse:
    return render(request, 'main/about.html')

def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'main/index.html')