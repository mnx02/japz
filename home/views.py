from django.shortcuts import render, redirect, HttpResponse



from home.models import Register, Login, Profile
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout
from .forms import *
from django.contrib.auth.models import User

def register(request):
    if request.method == "POST":
         username = request.POST.get('username')
         email = request.POST.get('email')
         password = request.POST.get('password')
         confirmpassword = request.POST.get('confirmpassword')
         name = request.POST.get('name')
         dob = request.POST.get('dob')
         gender = request.POST.get('gender')
         city = request.POST.get('city')
         
         if len(username)>12:
             messages.error(request, 'Your account has been created successfully!')
             return redirect('register.html')
         if not username.isalnum():
             messages.error(request, 'Username should only contain Letters and Numbers')
             return redirect('register.html')
         if password != confirmpassword:
             messages.error(request, 'Password does not match')
             return redirect('register.html')
         
             
         
         myuser= User.objects.create_user(username, email, password)
         myuser.name =name
         myuser.dob = dob
         myuser.gender = gender
         myuser.city = city
         myuser.save()
         messages.success(request, 'Your account has been created successfully!')
         return redirect('login.html')
    return render(request, 'register.html')
def about(request):
    return render(request, 'about.html')
def handlelogin(request):
    if request.method == "POST":
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        
        user = authenticate(username=loginusername, password= loginpassword)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In!")
            return redirect('index.html')
        else:
            messages.error(request, "Invalid Credentials, Please Try Again")
            return redirect('login.html')
    return render(request, 'login.html')
def handlelogout(request):
    logout(request)
    messages.success(request, "Successfully Logges Out!")
    return redirect('login.html')
def index(request):
    return render(request, 'index.html')
def userchangepassword(request):
    return render(request, 'Change_password.html')
def closeaccount(request):
    return render(request, 'Close_account.html')
def videochat(request):
    return render(request, 'Videochat.html')
def worldchat(request):
    return render(request, 'worldchat.html')
def usernotification(request):
    return render(request, 'user-notification.html')
def settings(request):
    return render(request, 'user-setting.html')
def verifyaccount(request):
    return render(request, 'user-verify-account.html')
def contact(request):
    return render(request, 'contact.html')
def profile(request):
    return render(request, 'user-account-info.html')

    

