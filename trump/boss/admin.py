# users/admin.py
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import UserCreationForm, SignUpForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = SignUpForm
    form = SignUpForm
    model = CustomUser
    list_display = ['username', 'salary', 'year']

admin.site.register(CustomUser, CustomUserAdmin)