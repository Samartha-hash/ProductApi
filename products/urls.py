from django.urls import path
from .views import ProductAPIView

urlpatterns = [
    path('products/', ProductAPIView.as_view(), name='product_class_view'),
    path('products/<int:pk>/', ProductAPIView.as_view(), name='product_edit_delete_view'),
]
