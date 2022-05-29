from tkinter import CASCADE
from django.db import models
from users.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')

    def __str__(self) -> str:
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=100)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='item_subcategory')
    ean = models.IntegerField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name


class Purchase(models.Model):
    username = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    item = models.ForeignKey(Item, related_name='item_name', on_delete=models.CASCADE)
    price = models.IntegerField()
    amount = models.IntegerField()
    
    def __str__(self) -> str:
        return f'{self.username}, {self.created}'
