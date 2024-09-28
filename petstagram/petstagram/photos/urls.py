from django.urls import path, include
from petstagram.photos import views

urlpatterns = [
    path('add/', views.add_photo_view, name='add-photo'),
    path('<int:pk>/', include([
        path('', views.photo_details_view, name='photo-details'),
        path('edit/', views.edit_photo_view, name='edit-photo'),
    ]))
]
