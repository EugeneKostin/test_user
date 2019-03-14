from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from .forms import UserCreationForm, UserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ['email', 'password', 'username', 'second_name', 'first_name', 'last_name', 'birth_date', 'auth_key', 'created_at', 'update_at']

admin.site.register(User, CustomUserAdmin)