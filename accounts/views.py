from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
# Create your views here.

def UserLogin(request):
	if request.user.is_authenticated:
		return redirect('/')

	NEXT = request.GET.get('next')

	form = LoginForm(request.POST or None)
	if form.is_valid():
		human = True
		cd = form.cleaned_data
		user = authenticate(username=cd['username'], password=cd['password'])
		if user is not None:
			login(request, user)
			messages.success(request, 'you logged in successfully !', 'success')
			if NEXT:
				return redirect(NEXT)
			return redirect('/')
		else:
			message.error(request, 'NOT FOUND', 'warning')

	return render(request, 'accounts/login.html', {'form':form})

def UserLogout(request):
	if request.user.is_authenticated:
		logout(request)
		messages.success(request, 'you logged out successfully !', 'success')
		NEXT = request.GET.get('next')
		if NEXT:
			return redirect(NEXT)
	else:
		return redirect('/')

def nothing(request):
	return render(request, 'accounts/nothing.html')