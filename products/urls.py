from django.urls import path
from products.views import (
    ListProductsAPIView,
    CreateProductsAPIView,
     UpdateProductsAPIView,
     RetrieveProductsAPIView,
     DestroyProductsAPIView,
     RetrieveUpdateDestroyProductsAPIView,
     ProductsAPIView

)

urlpatterns = [
    path('products/', ListProductsAPIView.as_view(), name='products'),
    path('products/create/', CreateProductsAPIView.as_view(), name='products-create'),
    path('products/Update/<slug:slug>', UpdateProductsAPIView.as_view(), name='products-update'),
    path('products/Retrieve/<pk>', RetrieveProductsAPIView.as_view(), name='products-retrieve'),
    path('products/Destroy/<pk>', DestroyProductsAPIView.as_view(), name='products-destroy'),
    path('products/app/<pk>', RetrieveUpdateDestroyProductsAPIView.as_view(), name='products-app'), # write-delete-delete
    path('products/products/<pk>', ProductsAPIView.as_view(), name='products-mixin'), # Mixins

]
