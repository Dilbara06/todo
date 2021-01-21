from django.db import models

class Todo (models.Model):
    text=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    is_closed=models.BooleanField(default=False)
    is_favorite=models.BooleanField(default=False)


class Books (models.Model):
    title=models.CharField(max_length=100)
    subtitle=models.CharField(max_length=100)
    description=models.CharField(max_length=200)
    price=models.CharField(max_length=20)
    genre=models.CharField(max_length=100)
    author=models.CharField(max_length=200)
    year=models.CharField(max_length=10)
    date=models.DateField(auto_now_add=True)
    is_favorite=models.BooleanField(default=False)
 
