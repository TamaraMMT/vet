from django.contrib import admin
from .models import Category, PostBlog

class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(PostBlog)
class PostAdmin(admin.ModelAdmin):
    ...


admin.site.register(Category, CategoryAdmin)



