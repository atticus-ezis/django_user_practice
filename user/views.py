from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth import login


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # redirect('profile')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form':form})


# Create your views here.
