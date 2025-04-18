from django.contrib import admin
from django.urls import path
from .views import home_view, about_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home_view),
    path('home/', home_view, name='home'),
    path("about/", about_view),
]
