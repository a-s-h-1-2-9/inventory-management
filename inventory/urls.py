# inventory/urls.py
from django.urls import path
from .views import InventoryItemViewSet, UserRegistrationView, CustomTokenObtainPairView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'inventory-items', InventoryItemViewSet)

urlpatterns = [
    path('adminuser/register/', UserRegistrationView.as_view(), name='register'),
    path('adminuser/logintoken/', CustomTokenObtainPairView.as_view(), name='logintoken'),
] + router.urls
