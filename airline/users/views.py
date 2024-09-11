from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

def index(request):
    if not request.user.is_authenticated:
        return render(request, "users/login.html", {
            "message": "Login required."
        })
    
    return render(request, "users/index.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is None:
            return render(request, "users/login.html", {
                "message": "User not found."
            })
        
        login(request, user=user)

        return render(request, "users/index.html", {
            "message": "You logged in succesfuly"
        })
    
    return render(request, "users/login.html")

def logout_view(request):
    logout(request=request)
    return HttpResponseRedirect(reverse("login"))
