from django.urls import path, include
from forumApp.posts import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('dashboard/', views.DashboardView.as_view(), name='dash'),
    path('add-post/', views.AddPostView.as_view(), name='add_post'),
    path('<int:pk>/', include([
        path('', views.post_details, name='post_details'),
        path('delete/', views.DeletePostView.as_view(), name='delete_post'),
        path('edit/', views.EditPostView.as_view(), name='edit_post'),
    ]))
]
