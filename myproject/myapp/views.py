from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Author, Book, Publisher
from .forms import AuthorForm, BookForm, PublisherForm

def home(request):
    return render(request, 'myapp/home.html')

def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AuthorForm()
    return render(request, 'myapp/add_author.html', {'form': form})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm()
    return render(request, 'myapp/add_book.html', {'form': form})

def add_publisher(request):
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PublisherForm()
    return render(request, 'myapp/add_publisher.html', {'form': form})

def search(request):
    query = request.GET.get('q')
    results = []
    if query is not None:
        results = Book.objects.filter(title__icontains=query)
    return render(request, 'myapp/search.html', {'results': results})