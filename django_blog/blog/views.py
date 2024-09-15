from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm  
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')  # Redirect to profile after registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})


def profile(request):
    if request.method == 'POST':
        user = request.user
        user.email = request.POST.get('email')
        user.save()
        return redirect('profile')  
    return render(request, 'blog/profile.html')