from django.shortcuts import render
from .models import *

def homepage(request):
    elements = Element.objects.all()
    return render(request, 'homepage.html', {
        'elements': elements,
    })
