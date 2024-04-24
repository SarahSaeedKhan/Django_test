from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,

)

from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin

from products.models import Products
from products.serializers import ProductsSerializer


class ListProductsAPIView(ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class CreateProductsAPIView(CreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class RetrieveProductsAPIView(RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class UpdateProductsAPIView(UpdateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    lookup_field = 'slug'


class DestroyProductsAPIView(DestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class RetrieveUpdateDestroyProductsAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class ProductsAPIView(ListModelMixin, CreateModelMixin, DestroyModelMixin):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    lookup_field = 'slug'
