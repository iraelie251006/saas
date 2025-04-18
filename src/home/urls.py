from django.contrib import admin
from django.urls import path
from .views import home_page_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_page_view, name='home'),
]
