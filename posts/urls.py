from django.urls import path

from posts import views

urlpatterns = [
    path('', views.index),
    path('posts/', views.posts),
    path('posts/<slug>', views.specific_post)
]
