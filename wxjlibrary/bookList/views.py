from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from django_filters import rest_framework as filters
from bookList import models
from . import serializers

class ProductFilter(filters.FilterSet):
    class Meta:
        model = models.Post
        fields = ['name',]
		
class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = ProductFilter
    filter_backends = (SearchFilter,filters.DjangoFilterBackend)
    search_fields = ('name','author')

class StarViewSet(viewsets.ModelViewSet):
    queryset = models.Star.objects.all()
    serializer_class = serializers.StarSerializer

