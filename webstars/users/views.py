from django.shortcuts import render, redirect
from .forms import userRegistrationForm, userUpdateForm, profileUpdateForm
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


# Create your views here.


def login(request):
    
    return render(request, 'webstarsapp/login.html')

def signup(request):
    if request.method == "POST":
        form = userRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, F'Hello, {username}? Your account has been created. Log in now')
            
            return redirect('login')

    else:
        form = userRegistrationForm()

    return render(request, 'webstarsapp/signup.html', {'form':form})

def logout(request):
    if request.method == "POST":
        logout(request)

    return redirect('home')

@login_required()
def profile(request):

    if request.method == 'POST':
        u_form = userUpdateForm(request.POST, instance=request.user)
        p_form = profileUpdateForm(request.POST,
            request.FILES,
            instance=request.user.profile)
        
        if u_form.is_valid and p_form.is_valid:
            u_form.save()
            p_form.save()
            
            messages.success(request, F'Hi,your profile info has been updated!')
            return redirect('profile')
    
    else:
        u_form = userUpdateForm(instance=request.user)
        p_form = profileUpdateForm(instance=request.user.profile)

    context = {
        'u_form':u_form,
        'p_form':p_form
    }


    return render(request, 'webstarsapp/profile.html', context)
