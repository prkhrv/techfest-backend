from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username','first_name','last_name','phone','roll','branch','email','section','year')

    def clean_email(self):
        email = self.cleaned_data.get('email')

        try:
            match = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return email
        raise forms.ValidationError('This Email is Already in Use')        

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username','first_name','last_name','phone','roll','branch','email','section','year')
