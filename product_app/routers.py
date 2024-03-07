from rest_framework.routers import DefaultRouter
from .views import PRODUCTViewSet

router = DefaultRouter()

router.register('product', PRODUCTViewSet)