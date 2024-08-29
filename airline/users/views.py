from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

def index(require):
    if not require.user.is_authenticated:
        return render(require, "users/login.html", {
            "message": "Login required."
        })
        
    return render(require, "users/index.html", {
        
    })
    
        
def login_view(require):
    if require.method == 'POST':
        username = require.POST['username']
        password = require.POST['password']
        user = authenticate(require, username=username, password=password)
        if user is None:
            return render(require, "users/login.html", {
                "message": "User not found."
            })
            
        login(require, user=user)
        return render(require, "users/index.html", {
            "message": "Login successfuly.",
        })
            
    return render(require, "users/login.html")
        
def logout_view(require):
    logout(require)
    return HttpResponseRedirect(reverse('login'))

