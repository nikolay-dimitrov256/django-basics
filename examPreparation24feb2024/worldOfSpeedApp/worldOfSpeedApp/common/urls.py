from django.urls import path
from worldOfSpeedApp.common import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]