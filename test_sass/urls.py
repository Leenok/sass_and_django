from django.contrib import admin
from django.urls import path
from test_sass import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sass_page', views.sass_page_handler),
]