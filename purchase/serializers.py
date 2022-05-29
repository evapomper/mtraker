from rest_framework import serializers

from .models import Purchase, Category, SubCategory, Item


class PurchaseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Purchase
        fields = ('id', 'username', 'item', 'price', 'amount', 'created',)
        

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ('id', 'name',)
        

class SubCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SubCategory
        fields = ('id', 'name', 'category',)
        

class ItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Item
        fields = ('id', 'name', 'subcategory', 'ean',)
        