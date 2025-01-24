from django.shortcuts import render
from .models import Post
from django.http import HttpResponse
def test(request):
  return render(request,'blog/base.html')

def login(request):
  return render(request, 'blog/login.html')

def signup(request):
  return render(request,'blog/signup.html')   

def home(request):
  context={
    'posts':Post.objects.all()
  }
  return render(request, 'blog/home.html',context)

# Create your views here.
