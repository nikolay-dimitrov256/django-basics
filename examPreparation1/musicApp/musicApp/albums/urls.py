from django.urls import path, include

from musicApp.albums import views

urlpatterns = [
    path('add/', views.AddAlbumView.as_view(), name='add-album'),
    path('<int:id>/', include([
        path('details/', views.AlbumDetailsView.as_view(), name='album-details'),
        path('edit/', views.AlbumEditView.as_view(), name='edit-album'),
        path('delete/', views.AlbumDeleteView.as_view(), name='delete-album'),
    ]))
]