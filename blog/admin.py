from django.contrib import admin
from .models import Category, PostBlog


class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(PostBlog)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'created_ad']
    list_display_links = 'id', 'title', 'author', 'created_ad'
    search_fields = 'id', 'title', 'description', 'author'
    list_filter = 'category', 'author', 'created_ad'
    list_per_page = 10
    prepopulated_fields = {
        'slug': ('title',)
    }


admin.site.register(Category, CategoryAdmin)
