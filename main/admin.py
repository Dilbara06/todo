from django.contrib import admin
from .models import Todo
from .models import Books

admin.site.register(Todo)
admin.site.register(Books)
