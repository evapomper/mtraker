from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import PurchaseViewSet, ItemViewSet, CategoryViewSet, SubCategoryViewSet


router = SimpleRouter()
router.register('purchase', PurchaseViewSet, basename='purchase')
router.register('item', ItemViewSet, basename='item')
router.register('category', CategoryViewSet, basename='category')
router.register('subcategory', SubCategoryViewSet, basename='subcategory')

urlpatterns = router.urls