from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse_lazy
from .models import User
from .forms import UserCreationForm, UserChangeForm, UserLoginForm
from django.contrib.auth.hashers import make_password
from datetime import datetime  
from django.contrib.auth.forms import SetPasswordForm 


def index(request):
    return render(request, "index.html")


def UserRegistrationForm(request):
	template_name = 'templates/registration.html'
	if request.method == 'POST':
		user_form = UserCreationForm(data=request.POST)
		if user_form.is_valid():
			user = user_form.save()
			user.save()
			return redirect('login')
		else:
			password = User.objects.make_random_password()
			if user_form.is_valid():
				user = user_form.save()
				user.save()
				return redirect('login')
			else:
				print(user_form.errors)
				return redirect('registration')
	else:
		user_form = UserCreationForm()
		return render(request,'templates/registration.html',
                          {'user_form':user_form})

def edit_user(request):
	template_name = 'templates/edit.html'
	if request.method == 'POST':
			user_form = UserChangeForm(request.POST, instance=request.user)
			if user_form.is_valid():
				user = user_form.save()
				user.update_at = datetime.now()
				user.save()
				messages.success(request, 'You have successfully edit')
				return redirect('edit')
			else:
				messages.error(request, 'Ошибка данных')
				return redirect('edit')

	else:
		user_form = UserChangeForm(instance=request.user)
		return render(request,'templates/edit.html',
	                          {'user_form':user_form})

		     

def delete_user(request):
		    try:
		        username = request.user.username
		        user = User.objects.get(username = username)
		        user.delete()
		        return HttpResponseRedirect("/")
		    except User.DoesNotExist:
		        return HttpResponseNotFound("<h2>User not found</h2>")

def login_user(request):
    if request.method == 'POST':
    	form = UserLoginForm(data = request.POST)
    	if form.is_valid():
        	username = form.cleaned_data['username']
        	password = form.cleaned_data['password']
        	user = authenticate(request, username=username, 
        		password=password)
        	if user:
        		#if user.is_active:
		            login(request, user)
		            messages.success(request, 'You have successfully logged in')
		            return redirect('index')
	        else:
	            messages.error(request, 'Ошибка входа')
	            return redirect('login')
    else:
        return render(request, 'login.html', {})

def logout_user(request):
	logout(request)
	return render(request, 'index.html')

def forgotPassword(request):
	if request.method == 'POST':
		username=request.POST.get("username")
		user = User.objects.get(username=username)
		if user:
			
			return redirect('passwordreq')
		else:
			print ("No user")
			return redirect('reppassword')
	else:
		return render(request, 'forgotPassword.html')

def passwordRecovery(request):
    if request.method == 'POST':
        form = SetPasswordForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            messages.error(request, "Error")
            return redirect('passwordreq')
    else:
        form = SetPasswordForm(user=request.user)
        return render(request, 'passwordRecovery.html', {'form': form})