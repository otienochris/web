from django.shortcuts import render, redirect
from .forms import userRegistrationForm
from django.contrib import messages

# Create your views here.


def login(request):
    
    return render(request, 'webstarsapp/login.html')

def signup(request):
    if request.method == "POST":
        form = userRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, F'Account created for {username}')
            return redirect('profile')

    else:
        form = userRegistrationForm()

    return render(request, 'webstarsapp/signup.html', {'form':form})