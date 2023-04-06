from django.contrib import admin
from .models import Board, Category

# Register your models here.
class BoardAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ['title', ]

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ['name', ]

admin.site.register(Board, BoardAdmin)
admin.site.register(Category, CategoryAdmin)