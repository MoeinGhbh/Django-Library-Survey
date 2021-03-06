from django.contrib import admin
from . import models

class BooksInstanceInline(admin.TabularInline):
    model = models.BookInstance

# Decorate
# admin.site.register(models.Author ,AuthorAdmin )
@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

# admin.site.register(models.Book)
@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    list_filter = ('title', 'author')
    inlines = [BooksInstanceInline]


# admin.site.register(models.Genre)
@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

# admin.site.register(models.BookInstance)
@admin.register(models.BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )



