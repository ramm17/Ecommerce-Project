from .views import *
from django.urls import path

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('category/<slug>', CategoryView.as_view(), name='category'),
    path('detail/<slug>', ProductDetailView.as_view(), name='detail'),
    path('product_review', product_review, name='product_review'),
]