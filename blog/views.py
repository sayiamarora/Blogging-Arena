from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('usname')
        email = request.POST.get('uemail')
        password = request.POST.get('upassword')
        if not username or not email or not password:
            return render(request, 'blog/signup.html', {'error': 'All fields are required.'})
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return redirect('/login')
        except Exception as e:
            return render(request, 'blog/signup.html', {'error': str(e)})
    
    return render(request, 'blog/signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('upassword')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/home')
        else:
            return render(request, 'blog/login.html', {'error': 'Invalid username or password.'})

    return render(request, 'blog/login.html')

def home(request):
    return render(request, 'blog/home.html')
