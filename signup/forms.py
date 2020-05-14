from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from . models import Profile




class SignUpForm(UserCreationForm):
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'birth_date', 'password1', 'password2','email' )


class user_loginform(forms.Form):

    username=forms.CharField(max_length=500)
    password=forms.PasswordInput(max_length=200)
