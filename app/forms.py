from django import forms
from .models import Projects

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ('title','description','tasks','peoples','end_time','status')


class RegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email")

    class Meta:
        model = User
        fields = ('username','email','password1','password2')
