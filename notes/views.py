from django.shortcuts import render, redirect
from .forms import CreateNoteForm


def create_note(request, username):
    if request.method == 'POST':
        form = CreateNoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('profile', username=username)
    else:
        form = CreateNoteForm()
    context = {'form':form, 'username':username}
    return render(request, 'notes/create_note.html', context)

