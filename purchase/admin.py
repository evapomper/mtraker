import imp
from django.contrib import admin
from .models import Category, SubCategory, Item, Purchase


admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Item)
admin.site.register(Purchase)