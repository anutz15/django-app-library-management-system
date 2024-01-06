from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.models import User
from .models import Student

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password1','password2']
class StudentRegisterForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["roll_no", "branch"]

class OTPForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["roll_no", "otp"]

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']