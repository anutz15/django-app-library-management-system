from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Book
from django.views.decorators.csrf import csrf_exempt

def about(request):
    return render(request, 'about.html')



@login_required(login_url='account-login')
@csrf_exempt
def catalog(request):
    books = Book.objects.all()
    return render(request, 'catalog.html', {'books': books})

@login_required(login_url='account-login')
def search(request):
    title = request.GET.get('title')
    author = request.GET.get('author')
    publisher = request.GET.get('publisher')

    books = Book.objects.all()
    if title:
        books = books.filter(title__icontains=title)
    if author:
        books = books.filter(author__icontains=author)
    if publisher:
        books = books.filter(publisher__icontains=publisher)

    return render(request, 'catalog.html', {'books': books})

