from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Team

# Create your views here.

def places(request):
    obj=Place.objects.all()
    # name='india'
    return render(request,"index.html",{'result':obj})

def teams(request):
    seg=Team.objects.all()
    return render(request,"index.html",{'teams':seg})

    # return render(request,"home.html",{'obj':name})
# def addition(request):
#     num1=int(request.GET['num1'])
#     num2=int(request.GET['num2'])
#     res=num1+num2
#     return  render(request,"result.html",{'result':res})
# def about(request):
#     return render(request,"about.html")
#
# def contact(request):
#     return HttpResponse("hello am contact")