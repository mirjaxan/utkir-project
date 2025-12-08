from django.urls import path
from .views import post_detail,home

urlpatterns = [
    path("", home, name="home"),
    path('post/<slug:slug>/', post_detail, name='detail'),

    # path('add/', views.post_create, name='post_create'),
    # path('update/<int:pk>/', views.post_update, name='post_update'),
    # path('delete/<int:pk>/', views.post_delete, name='post_delete'),
]
