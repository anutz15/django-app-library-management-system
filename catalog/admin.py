from django.contrib import admin
from .models import Book

class AdminBook(admin.ModelAdmin):
    def available(self, obj):
        return obj.number_of_copies_available
    available.short_description = "Available Copies"

    def issued(self, obj):
        return obj.number_of_copies - obj.number_of_copies_available
    issued.short_description = "Issued Copies"

    def total(self, obj):
        return obj.number_of_copies
    total.short_description = "Total Copies"

    def has_ebook(self, obj):
        return obj.ebook != None and obj.ebook != "" and obj.ebook != " "
    has_ebook.boolean = True
    has_ebook.short_description = "E-book"

    list_display = ('title', 'author', 'publisher', 'available', 'issued', 'total', 'has_ebook')
    search_fields = ('title', 'author', 'publisher')

admin.site.register(Book, AdminBook)
