from rest_framework import viewsets, permissions

from .models import Category, Item, Purchase, SubCategory
from mtracker_project.permissions import IsUserOrReadOnly
from .serializers import PurchaseSerializer, CategorySerializer, SubCategorySerializer, ItemSerializer


class PurchaseViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer


class ItemViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubCategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


