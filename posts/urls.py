from django.urls import path

from posts import views

urlpatterns = [
    path('', views.index, name="index"),
    path('posts/', views.posts, name="posts"),
    path('posts/<slug>', views.specific_post, name="specific")
]
