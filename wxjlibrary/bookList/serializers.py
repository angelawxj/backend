from rest_framework import serializers
from . import models


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name', 'author', 'img_url')
        model = models.Post

class StarSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name', 'author', 'img_url','is_have')
        model = models.Star

