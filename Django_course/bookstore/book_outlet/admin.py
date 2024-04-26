from django.contrib import admin

from .models import Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):
   readonly_fields = ("slug",)
   list_filter = ("author", "rating",)
   list_display = ("title", "author",)

admin.site.register(Book, BookAdmin)