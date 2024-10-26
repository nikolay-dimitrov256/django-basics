from django.urls import path
from musicApp.profiles import views

urlpatterns = [
    path('details/', views.ProfileDetailsView.as_view(), name='profile-details'),
]