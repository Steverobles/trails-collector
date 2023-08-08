from django.shortcuts import render
from .models import Trail

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def trails_index(request):
    trails = Trail.objects.all()
    return render(request, 'trails/index.html', {
        'trails':trails
    })

def trails_detail(request,trail_id):
    trail = Trail.objects.get(id=trail_id)
    return render(request, 'trails/details.html', {'trail':trail})