from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegistrationForm, UserUpdateForm

# Create your views here.

def register(request):
	form = UserRegistrationForm()
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, f'Account created for {username}!')
			return redirect('home')
	context = {'form': form}
	return render(request, 'users/register.html', context)

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f'Account info updated!')
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)

    context = {
        'form': form,
    }

    return render(request, 'users/profile.html', context)
