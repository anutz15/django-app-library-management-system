from django.urls import path
from .views import register, otp
from .views import user_login, user_logout
from .views import profile

urlpatterns = [
    path('register/', register, name="account-register"),
    path('otp/', otp, name="account-otp"),
    path('login/', user_login, name="account-login"),
    path('logout/', user_logout, name="account-logout"),
    path('profile/', profile, name="account-profile"),
]
