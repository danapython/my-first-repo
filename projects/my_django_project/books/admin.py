from django.contrib import admin
from .models import Author, Book

# Register your models hoere.

admin.site.register(Book)
admin.site.register(Author)
