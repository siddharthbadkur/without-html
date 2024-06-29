from django.shortcuts import render
from .forms import *
# Create your views here.

def home(request):
    new={}
    new['form']=Studentform
    return render(request,'home.html',new)
