from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import ProductListCreateView, ProductRetrieveUpdateDestroyView, StockListCreateView, StockRetrieveUpdateDestroyView

urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-detail'),
    path('stocks/', StockListCreateView.as_view(), name='stock-list'),
    path('stocks/<int:pk>/', StockRetrieveUpdateDestroyView.as_view(), name='stock-detail'),
]
