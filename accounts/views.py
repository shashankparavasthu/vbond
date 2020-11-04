from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.views.decorators.cache import cache_control

# Create your views here.

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login(request):

    if(request.method == 'POST'):
        #post the username and password to server
        uname = request.POST['uname']
        psw = request.POST['psw']
        # print(uname, " : ", psw )
        user = auth.authenticate(username = uname, password = psw)
        
        if user is not None:
            #user exists; successful login
            auth.login(request, user)
            return redirect('home')
        else:
            #invalid login credentials 
            messages.info(request, 'invalid credentials')
            return redirect('login') 
        
        return render(request, 'login.html')
    else:

        if request.user.is_authenticated:
            return redirect('home')
        else:
            #for GET , server returns the login page
            return render(request, 'login.html')
     
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout(request):
    auth.logout(request)
    return redirect('login')
