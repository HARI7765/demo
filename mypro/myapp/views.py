from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def index(request):
    if request.POST:
        name=request.POST.get('name')
        email=request.POST.get('email')
        obj1=detail(name=name,email=email)
        obj1.save()
    return render(request,"index.html")
def main(request):
    obj=detail.objects.all()
    return render(request,"main.html",{"det":obj})
def first(request):
    return render(request,"first.html")
def second(request):
    return render(request,"second.html")