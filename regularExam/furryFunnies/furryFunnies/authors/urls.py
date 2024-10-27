from django.urls import path
from furryFunnies.authors import views

urlpatterns = [
    path('create/', views.CreateAuthorView.as_view(), name='create-author'),
    path('details/', views.DetailsAuthorView.as_view(), name='details-author'),
    path('edit/', views.EditAuthorView.as_view(), name='edit-author'),
    path('delete/', views.DeleteAuthorView.as_view(), name='delete-author'),
]