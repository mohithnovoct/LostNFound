from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('lost/', views.lost_items, name='lost_items'),
    path('found/', views.found_items, name='found_items'),
    path('item/<int:pk>/', views.item_detail, name='item_detail'),
    path('item/new/', views.create_item, name='create_item'),
    path('my-posts/', views.user_posts, name='user_posts'),
    path('register/', views.register, name='register'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]