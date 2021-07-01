from django.urls import path
import rest_framework
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('', views.store, name='store'),
    path('get/', views.ProductList.as_view()),
]