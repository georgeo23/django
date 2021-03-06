from django.shortcuts import render, HttpResponse
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Books, Authors
from django.contrib.auth.decorators import login_required
from .forms import NewBookForm

# books =[
    
#     { 'id': 1, 'title': 'Life, the Universe and Everything', 'author': 'Douglas Adams'},
#     { 'id': 2, 'title': 'The Meaning of Liff', 'author': 'Douglas Adams'},
#     { 'id': 3, 'title': 'The No. 1 Ladie\'s Detective Agency', 'author': 'Alexander McCall Smith'}

# ]

# Create your views here.

def index(request):
    context = {'books': Books.objects.all()}
    return render(request, 'books/index.html', context)

@login_required
def show(request, book_id):
    context = {'book' : Books.objects.get(pk=book_id)}
    return render(request, 'books/show.html', context)

def error404(request): 
    return HttpResponse('Sorry, that page doesnt exist!')

@login_required
def create(request):
    if request.method == 'POST':
        Books = NewBookForm(request.POST)
        if Books.is_valid():
            book_id = Books.save().id
            return HttpResponseRedirect(f'/books/{book_id}')
    else:
        form = NewBookForm()
    data = {'form': form}        
    return render(request, 'books/new.html', data)