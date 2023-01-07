from django.contrib import admin
from .models import Blog, Book, SinglePage


@admin.register(SinglePage)
class SinglePageAdmin(admin.ModelAdmin):
    list_display = ('P_id', 'Page_name', 'Page_date', 'Page_author', )


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('Bk_id', 'Book_name', 'Book_pub_date',
                    'Book_price', 'author_names', )


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('B_id', 'Blog_name', 'Blog_pub_date', 'Blog_author', )
