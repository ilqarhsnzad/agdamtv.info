from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from news.models import Category, News

class CategorySerializer(ModelSerializer):
    class Meta:
        model=Category
        fields="__all__"

class NewsSerializer(ModelSerializer):
    # category=serializers.StringRelatedField()
    class Meta:
        model=News
        fields="__all__"