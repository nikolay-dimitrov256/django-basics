from django.urls import path, include
from petstagram.photos import views


urlpatterns = [
    path('add/', views.AddPhotoView.as_view(), name='add_photo'),
    path('<int:pk>/', include([
        path('', views.PhotoDetailsPage.as_view(), name='photo_details'),
        path('edit/', views.EditPhotoPage.as_view(), name='edit_photo'),
        path('delete/', views.delete_photo, name='delete_photo'),
    ])),
]
