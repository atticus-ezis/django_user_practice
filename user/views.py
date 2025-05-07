from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            redirect('profile')
    else:
        form = SignupForm()
    return render(request, 'user/signup.html', {'form':form})

@login_required
def profile(request):
    user = request.user
    return render(request, 'user/profile.html', {'user':user})



# Create your views here.


