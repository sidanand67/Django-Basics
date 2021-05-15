from django.urls import path 
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.ArticleCreateView.as_view(), name='article_create'),
    path('list/', views.ArticleListView.as_view(), name='article_list'),
    path('list/<int:pk>/', views.ArticleDetailView.as_view(), name='article_detail'),
    path('list/<int:pk>/update/', views.ArticleUpdateView.as_view(), name='article_update'),
    path('list/<int:pk>/delete', views.ArticleDeleteView.as_view(), name='article_delete'),
]