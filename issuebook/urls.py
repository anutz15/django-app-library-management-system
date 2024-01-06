from django.contrib import admin
from django.urls import path, include
from issuebook import views

urlpatterns = [
path("issuebook/<str:bookid>",views.issuebooknow)
]
