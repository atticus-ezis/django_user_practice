from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignupForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from notes.models import Note


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile', username=user.username)
    else:
        form = SignupForm()
    return render(request, 'user/signup.html', {'form':form})

def profile_redirect(request):
    return redirect('profile', username=request.user.username)

def profile(request, username):
    user = get_object_or_404(User, username=username)
    notes = Note.objects.filter(user=user)
    context ={'user':user, 'notes':notes}
    return render(request, 'user/profile.html', context)






