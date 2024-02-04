from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/', views.catalog, name='catalog'),
    path('about_products/', views.about_products, name='about_products'),
    path('aroma_oil/', views.aroma_oil, name='aroma_oil'),
    path('master_class/', views.master_class, name='master_class'),
    path('master_cass_confirm/', views.master_cass_confirm, name='master_cass_confirm'),
    path('gift_certificate/', views.gift_certificate, name='gift_certificate'),
    path('reviews/', views.reviews, name='reviews'),
]
