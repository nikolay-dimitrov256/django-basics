from django.urls import path
from petstagram.common import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('like/<int:photo_id>/', views.like_functionality, name='like')
]
