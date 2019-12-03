from django.contrib import admin
from p_library.models import Book, Author, Redaction, BooksRent

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    @staticmethod
    def author_full_name(obj):
        return obj.author.full_name

    list_display = ('title', 'author_full_name',)
    fields = ('ISBN', 'title', 'preview', 'description', 'year_release', 'author', 'price', 'redaction')
    list_filter = ('author', 'redaction',)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Redaction)
class RedactionAdmin(admin.ModelAdmin):
    pass

@admin.register(BooksRent)
class BooksRentAdmin(admin.ModelAdmin):
    list_display = ('book_renter', 'rented_book',)