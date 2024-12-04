from django.contrib import admin

# Register your models here.
from .models import Author, Book, Genre, PublishingHouse, Reader, Loan

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(PublishingHouse)
admin.site.register(Reader)
admin.site.register(Loan)