from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

from .decorators import login_requires
from .forms import NewUserForm, ChangeProfile
from .models import User, Profile

@login_requires
def homeView(request):
    print("wtf")
    
    prof = Profile.objects.get(user=request.user)
    
    #form = ChangeProfile
    if request.method == "POST":
        proName = request.POST['proName']
        print(proName)
        prof.name = proName

        #form = ChangeProfile(request.POST)
        #if form.is_valid:
        #    obj = form.save(commit=False)

    return render(request, "authapp/home.html", {"name":prof})

def signupView(request):
    if request.user.is_authenticated:
        return redirect('/')

    form = NewUserForm
    users = User.objects.all()
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()

            """
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=password)

            print("user auth")
            print(user.username)
            
            login(request, user)
            """
            return render(request, "authapp/signin.html")

    return render(request, "authapp/signup.html", {'form':form, 'users':users})


def signinView(request):

    #redirect loggedin user to the same page
    if request.user.is_authenticated:
        print("(x)")
        return redirect('/')

    if request.method == "POST":
        print("[x]")
        
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        print("user")
        print(user)
        print(type(user))
        if user is not None:
            login(request, user)
            return redirect('/')

    users = User.objects.all()
    names = Profile.objects.all()
    context = {"users":users, "names":names}
    return render(request, "authapp/signin.html", context)

def signoutView(request):
    logout(request)
    return redirect('/')