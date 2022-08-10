from django.contrib import admin

from .models import Post, Contact

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date', 'content')
    list_display_links = ('title', 'author', 'date', 'content')
    list_filter = ('title', 'author', 'date', 'content')
    search_fields = ('title', 'author', 'date', 'content')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    model = Contact