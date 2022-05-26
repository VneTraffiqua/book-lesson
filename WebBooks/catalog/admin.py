from django.contrib import admin
from .models import Autor, Book, Genre, Language, Status, BookInstance

# Register your models here.
#admin.site.register(Autor)
#admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Status)
#admin.site.register(BookInstance)

# определения к классу администратор
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')
    fields = ['first_name', 'last_name',('date_of_birth', 'date_of_death')]

# Зарегестрируйте класс admin с соотвествующей моделью
admin.site.register(Autor, AuthorAdmin)

class BooksInstanceInLine(admin.TabularInline):
    model = BookInstance

# Регистрируем классы администратора для книг
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'language', 'display_author')
    list_filter = ('genre', 'author')
    inlines = [BooksInstanceInLine]

# Регистрируем классы администратора для экземпляра книги
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('book', 'status')
    fieldsets = (
        ('Экземпляр книги', {
            'fields': ('book', 'imprint', 'inv_nom')
        }),
        ('Статус и окончание его действия', {
            'fields': ('status', 'due_back', 'borrower')
        })
    )

