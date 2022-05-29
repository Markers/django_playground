from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from .forms import CreateUserForm

# Create your views here.


def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['username'],
                                            password=request.POST.get(
                                                'password1', False),  # ['passoword1'],
                                            email=request.POST['email'],)
            auth.login(request, user)
            return redirect('/')
        return render(request, 'signup.html')
    return render(request, 'signup.html')


def signup2(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password1'],
                email=request.POST['email'],
            )
            auth.login(request, user)
            return redirect('/')
        return render(request, 'signup2.html')
    else:
        form = UserCreationForm
        return render(request, 'signup2.html', {'form': form})


def signup3(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request, 'signup2.html')
    context = {'form': form}
    return render(request, 'signup2.html', context)


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect'})
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('home')


def home(request):
    return render(request, 'home.html')
