from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:post_id>/', views.view_post, name='view_post'),
    path('<int:post_id>/upvote/', views.upvote, name='upvote')
]
