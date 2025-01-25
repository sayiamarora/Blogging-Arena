from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from .models import Post

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

@login_required
def home(request):
    # Fetch all posts to display on the home page
    posts = Post.objects.all().order_by('-id')  # Latest posts first
    return render(request, 'blog/home.html', {'posts': posts})

@login_required
def newPost(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if not title or not content:
            return render(request, 'blog/newpost.html', {'error': 'All fields are required.'})
        npost = Post(title=title, content=content, author=request.user)
        npost.save()
        return redirect('/home')
    return render(request, 'blog/newpost.html')

@login_required
def myPost(request):
    # Fetch posts authored by the logged-in user
    user_posts = Post.objects.filter(author=request.user).order_by('-id')
    return render(request, 'blog/mypost.html', {'posts': user_posts})

def signOut(request):
    logout(request)
    return redirect('/login')
