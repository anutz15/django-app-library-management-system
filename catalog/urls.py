from django.urls import path
from .views import catalog, search, about

urlpatterns = [
    path('', catalog, name='catalog-home'),
    path('search/', search, name='catalog-search'),
    path('about/',about)
]
