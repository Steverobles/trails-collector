from django.shortcuts import render
from .models import Trail

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def trails_index(request):
    return render(request, 'trails/index.html', {
        'trails':trails
    })