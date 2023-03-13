from django.contrib import admin
from .models import Contact, Category, Photo

# Register your models here.

admin.site.register(Contact)
admin.site.register(Photo)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
