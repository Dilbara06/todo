from django.shortcuts import render, HttpResponse, redirect
from .models import Todo
from .models import Books

# Create your views here.
def homepage(request):
    return render (request, "index.html")

def test(request):
    todo_list=Todo.objects.all()
    return render (request, "test.html", {"todo_list":todo_list})

def second(request):
    books_list=Books.objects.all()
    return render (request, "books.html", {"books_list":books_list})

def third(request):
    return HttpResponse ("This is page test 3")

def add_todo(request):
    form=request.POST
    text=form["todo_text"]
    todo=Todo(text=text)
    todo.save()
    return redirect(test)

def add_books (request):
    form=request.POST
    title=form["books_title"]
    subtitle=form["books_subtitle"]
    description=form["books_description"]
    price=form["books_price"]
    genre=form["books_genre"]
    author=form["books_author"]
    year=form["books_year"]
    books=Books(title=title,subtitle=subtitle,description=description,price=price,genre=genre,author=author,year=year)
    books.save()
    return redirect(second)

