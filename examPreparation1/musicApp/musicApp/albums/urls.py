from django.urls import path

from musicApp.albums import views

urlpatterns = [
    path('add/', views.AddAlbumView.as_view(), name='add-album'),
]