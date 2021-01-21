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

def detail(request):
    return render (request, "books_detail.html")

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

def delete_todo (request, id): 
     todo=Todo.objects.get(id=id)
     todo.delete()
     return redirect(test)

def mark_todo (request, id):
    todo=Todo.objects.get(id=id)
    todo.is_favorite=True
    todo.save()
    return redirect(test)

def unmark_todo (request, id):
    todo=Todo.objects.get(id=id)
    todo.is_favorite=False
    todo.save()
    return redirect(test)

def delete_books (request, id): 
     books=Books.objects.get(id=id)
     books.delete()
     return redirect(second)

def mark_books (request, id):
    books=Books.objects.get(id=id)
    books.is_favorite=True
    books.save()
    return redirect(second)

def unmark_books (request, id):
    books=Books.objects.get(id=id)
    books.is_favorite=False
    books.save()
    return redirect(second)

def BooksDetail (request, id): 
     books=Books.objects.get(id=id)
     return render (request, "books_detail.html",{"books":books} )

def close_todo (request, id):
    todo=Todo.objects.get(id=id)
    todo.is_closed=not todo.is_closed
    todo.save()
    return redirect(test)
    



     

