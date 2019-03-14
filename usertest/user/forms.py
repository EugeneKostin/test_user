from django import forms
from django.forms import CharField, PasswordInput
from .models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class UserCreationForm(UserCreationForm):
	class Meta(UserCreationForm):
		model = User
		fields = ('email', 'username', 'last_name', 'second_name', 'first_name',  'birth_date', 'auth_key')

class UserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'password', 'username', 'second_name', 'first_name', 'last_name', 'birth_date', 'auth_key')

class UserLoginForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'password']
		widgets = {'password':forms.PasswordInput()}

	def clean(self):
		return self.cleaned_data
