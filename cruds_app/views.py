from django.shortcuts import render
from .models import profile


# Create your views here.


def home(request):
    prof = profile.objects.all()
    return render(request, 'index.html', {'prof': prof})
