from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Team

# Create your views here.

def places(request):
    obj=Place.objects.all()
    seg=Team.objects.all()
    # name='india'
    return render(request,"index.html",{'result':obj,'teams':seg})




