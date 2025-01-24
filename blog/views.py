from django.shortcuts import render

from django.http import HttpResponse
def test(request):
  return render(request,'blog/base.html')

def login(request):
  return render(request, 'blog/login.html')

def signup(request):
  return render(request,'blog/signup.html')   

def home(request):
  return render(request, 'blog/home.html')

# Create your views here.
