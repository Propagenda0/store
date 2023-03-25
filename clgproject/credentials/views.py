from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def about(request):
    return render(request, 'about.html')
def message(request):
    return render(request, 'message.html')

def form(request):

    return render(request, 'form.html')


def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,"Invalid")
            return redirect('login')
    return render(request, 'login.html')

def register(request):
    if request.method== 'POST':
        username =request.POST['username']
        email =request.POST['email']
        password =request.POST['password']
        confirmpassword =request.POST['confirmpassword']
        if password==confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username is exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email is exists")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username, password=password, email=email)
                user.save();
                return redirect('login')
        else:
            messages.info(request, "Password is not match")
            return redirect('register')
        return redirect('/')
    return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

