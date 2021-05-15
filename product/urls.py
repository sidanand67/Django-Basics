from django.urls import path
from . import views

app_name="product"

urlpatterns = [
    path('', views.index, name='index'),
    path('result/', views.result, name='result'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),
]