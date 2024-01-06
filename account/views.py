from django.shortcuts import render, redirect
from django.core.mail import send_mail
import random

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import UserRegisterForm, StudentRegisterForm
from .forms import OTPForm
from .forms import UserLoginForm

def register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        student_form = StudentRegisterForm(request.POST)
        if user_form.is_valid() and student_form.is_valid():
            if User.objects.filter(username=student_form.cleaned_data['roll_no']).exists():
                student_form.add_error('roll_no', 'User with this roll number already exists')
            else:
                user = user_form.save(commit=False)
                user.username = student_form.cleaned_data['roll_no']
                user.is_active = False
                user.save()
                student = student_form.save(commit=False)
                student.user = user
                student.otp = str(random.randint(100000, 999999)) # 6 digit OTP
                student.save()
                try:
                    send_mail(
                        "Account Verification Code",
                        f"Your verification code is {student.otp}",
                        "dwijbavisi@gmail.com",
                        [user.email],
                    )
                    return redirect('account-otp')
                except:
                    pass
    else:
        user_form = UserRegisterForm()
        student_form = StudentRegisterForm()
    return render(request, 'register.html', {'user_form': user_form, 'student_form': student_form})

def otp(request):
    if request.method == 'POST':
        otp_form = OTPForm(request.POST)
        if otp_form.is_valid():
            roll_no = otp_form.cleaned_data['roll_no']
            if not User.objects.filter(username=roll_no).exists():
                otp_form.add_error('roll_no', 'User with this roll number does not exist')
            else:
                user = User.objects.get(username=roll_no)
                if user.student.otp != otp_form.cleaned_data['otp']:
                    otp_form.add_error('otp', 'Invalid OTP')
                else:
                    user.is_active = True
                    user.save()
                    user.student.otp = ''
                    user.student.save()
                    return redirect('account-login')
    else:
        otp_form = OTPForm()
    return render(request, 'otp.html', {'otp_form': otp_form})

def user_login(request):
    if request.method == 'POST':
        login_form = UserLoginForm(data = request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is None:
                login_form.add_error('username', 'Invalid Credentials')
            else:
                login(request, user)
                return redirect('catalog-home')
        else:
            username = login_form.cleaned_data['username']
            if not User.objects.filter(username=username).exists():
                login_form.add_error('username', 'User with this roll number does not exist')
            else:
                user = User.objects.get(username=username)
                if user.is_active == False:
                    login_form.add_error('username', 'This account is not active or verified')
                else:
                    login_form.add_error('password', 'Invalid Password')
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form': login_form})

def user_logout(request):
    logout(request)
    return redirect('account-login')

@login_required(login_url='account-login')
def profile(request):
    return render(request, 'profile.html')