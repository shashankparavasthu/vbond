from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.contrib.auth.models import User, auth

# Create your views here.
@login_required(login_url='login')
def home(request):
    if not request.user.is_authenticated:
            return redirect('login')
    return render(request, 'home.html')