from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from .forms import SignUpForm


# Create your views here.

def signup(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('course_list')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def my_login(request, username, password):

    if request.method == 'POST':

        form = AuthenticationForm(data = request.POST)

        if form.is_valid:

            user = form.get_user()

            login(request, user)

        return redirect('course_list')

    return render(request, 'login.html', {'form': form})
