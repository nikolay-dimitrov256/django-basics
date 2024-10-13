from django.urls import path, include
from forumApp.posts import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dash'),
    path('add-post/', views.add_post, name='add_post'),
    path('<int:pk>/', include([
        path('delete/', views.delete_post, name='delete_post'),
    ]))
]
