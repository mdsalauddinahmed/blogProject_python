from django.shortcuts import render
from post.models import post

def home(request):
    data = post.objects.all()
 
    return render(request,'home.html',{'data':data})