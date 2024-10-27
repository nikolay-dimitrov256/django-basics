from django.urls import path, include
from furryFunnies.posts import views

urlpatterns = [
    path('create/', views.CreatePostView.as_view(), name='create-post'),
    path('<int:post_id>/', include([
        path('details/', views.DetailsPostView.as_view(), name='details-post'),
        path('edit/', views.EditPostView.as_view(), name='edit-post'),
        path('delete/', views.DeletePostView.as_view(), name='delete-post'),
    ]))
]