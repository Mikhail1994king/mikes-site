from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

def hui(request):
    features = Feature.objects.all()
    return render(request, 'hui.html', {'features': features})