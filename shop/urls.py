# from django.urls import path
# from rest_framework_nested import routers
# from. import views


# router = routers.DefaultRouter()
# router.register('items', views.ItemViewSet)
# router.register('category', views.CategoryViewSet)


# category_router = routers.NestedDefaultRouter(router,'category', lookup='category')
# category_router = routers.register('items', views.ItemViewSet,  basename='category-items')

# urlpatterns = router.urls + category_router.urls



# urls.py

from django.urls import path
from rest_framework_nested import routers
from . import views

# Create the main router
router = routers.DefaultRouter()
router.register('items', views.ItemViewSet, basename='items')
router.register('category', views.CategoryViewSet)

# Create a nested router for handling images related to items
items_router = routers.NestedDefaultRouter(router, 'items', lookup='item')
items_router.register('images', views.ItemImageViewSet, basename='item-images')

# Combine the URL patterns from both routers
urlpatterns = router.urls + items_router.urls









    

