from django.urls import path, re_path, include

from urlsAndViews.departments import views

urlpatterns = [
    path('', views.index, name='home'),
    path('numbers/', include([   # include() works with lists as well
        path('<int:pk>/<slug:slug>', views.view_department),
        path('<int:pk>/', views.view_with_integer),
    ])),
    path('softuni/', views.redirect_to_softuni),
    path('redirect-to-view', views.redirect_to_view),
    path('<slug:slug>', views.view_with_slug),
    path('<param>/', views.view_with_variable),
    re_path(r'^archive/(?P<archive_year>202[0-3])/$', views.show_archive)
]
