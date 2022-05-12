from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('collestions', views.CollectionViewSet)
router.register('carts', views.CartViewSet)

products_router = routers.NestedSimpleRouter(router, 'products', lookup='product')
products_router.register('reviews', views.ReviewViewSet, basename='product-reviews')


urlpatterns = router.urls + products_router.urls
