from django.urls import path, include
from worldOfSpeedApp.cars import views
from worldOfSpeedApp.common.helpers import get_profile

urlpatterns = [
    path('create/', views.CreateCarView.as_view(), name='create-car'),
    path('catalogue/', views.CatalogueView.as_view(), name='catalogue'),
    path('<int:id>/', include([
        path('details/', views.CarDetailsView.as_view(), name='car-details'),
        path('edit/', views.CarEditView.as_view(), name='edit-car'),
    ]))
]