from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    fieldsets = ('Profile', {'fields': ('username','first_name','last_name','phone','roll','branch','email','section','year','is_staff','password',)}),
    list_display = ['username','first_name','last_name','email','is_staff',]

admin.site.register(CustomUser, CustomUserAdmin)
