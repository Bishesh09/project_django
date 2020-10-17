from django.contrib import admin
from apps.models import Book,Author 


@admin.register(Book)
class Bookadmin(admin.ModelAdmin):
	list_display=("name","isbn","price","author",)
	list_filter=("name","price")
	search_fields=("name","isbn",)
# Register your models here.


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
	list_display=("name","contact",)