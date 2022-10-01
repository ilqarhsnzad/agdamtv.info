from django.urls import path,include
from . import views
urlpatterns = [
    path('news',views.NewsListCreateAPIView.as_view(),name='news'),
    path('news/<int:pk>',views.NewsDetailAPIView.as_view(),name='news-detail'),
    
    path('categories',views.CategoryListCreateAPIView.as_view(),name='category'),
    path('categories/<int:pk>',views.CategoryDetailAPIView.as_view(),name='category-detail'),
    
    path('categories/<int:pk>/news',views.CategoryNewsListAPIView.as_view(),name='category-news')

]