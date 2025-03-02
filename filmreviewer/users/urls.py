from django.urls import path
from . import views

urlpatterns = [
  # User routes
  path('user/create_user/', views.create_user, name='create_user'),
  path('user/get_users/', views.get_users, name='get_users'),
  # Review routes
  path('review/create_review/', views.create_review, name='create_review'),
  path('review/get_reviews/', views.get_reviews, name='get_reviews'),
  path('review/get_review/', views.get_review_by_id, name='get_review'),
  path('review/update_review/', views.update_review, name='update_review'),
  path('review/delete_review/', views.delete_review, name='delete_review'),
]