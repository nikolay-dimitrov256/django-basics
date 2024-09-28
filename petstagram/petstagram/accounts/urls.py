from django.urls import path, include

from petstagram.accounts.views import register_view, login_view, profile_details_view, profile_edit_view, \
    profile_delete_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('profile/<int:pk>/', include([
        path('', profile_details_view, name='profile-details'),
        path('edit/', profile_edit_view, name='profile-edit'),
        path('delete/', profile_delete_view, name='profile-delete'),
    ]))
]
