from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,ListAPIView
from rest_framework.generics import get_object_or_404
from api.v1.serializers import CategorySerializer, NewsSerializer
from news.models import Category, News

class CategoryListCreateAPIView(ListCreateAPIView):
    serializer_class=CategorySerializer
    queryset=Category.objects.all()

class CategoryDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class=CategorySerializer
    queryset=Category.objects.all()

class NewsListCreateAPIView(ListCreateAPIView):
    serializer_class=NewsSerializer
    queryset=News.objects.all()

class NewsDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class=NewsSerializer
    queryset=News.objects.all()

class CategoryNewsListAPIView(ListAPIView):
    serializer_class=NewsSerializer
    def get_queryset(self):
        category=get_object_or_404(Category)
        return News.objects.filter(category=category)