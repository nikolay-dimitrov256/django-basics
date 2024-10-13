from django.urls import path, include
from petstagram.accounts import views


urlpatterns = [
    path('register/', views.register, name='register_account'),
    path('login/', views.login, name='account_login'),
    path('profile/<int:pk>/', include([
        path('', views.details, name='profile_details'),
        path('edit/', views.edit, name='profile_edit'),
        path('delete/', views.delete, name='profile_delete'),
    ]))
]