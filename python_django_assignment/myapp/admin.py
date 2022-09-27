from django.contrib import admin
from . models import Location, Category, Property

# Register your models here.
@admin.register(Location)
class LocationModel(admin.ModelAdmin):
    list_display = ['location_name']

@admin.register(Category)
class CategoryModel(admin.ModelAdmin):
    list_display = ['type']

@admin.register(Property)
class PropertyModel(admin.ModelAdmin):
    list_display = ['title', 'price']