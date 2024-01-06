from django.contrib import admin
from django.urls import path, include
from duebooks import views

urlpatterns = [
    path('checkduebooks', views.showduebooks),
    path('payfees',views.payduefees),
    path('howmuch',views.whichpay)

]
