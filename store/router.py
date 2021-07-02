from . import viewsets
from rest_framework import routers

router = routers.DefaultRouter()
router.register('product', viewsets.ProductViewset)
router.register('category', viewsets.CategoryViewset)