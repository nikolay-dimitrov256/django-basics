from django.urls import path
from worldOfSpeedApp.profiles import views

urlpatterns = [
    path('create/', views.ProfileCreateView.as_view(), name='create-profile'),
]