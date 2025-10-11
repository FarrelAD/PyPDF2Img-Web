from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('convert/', views.convert_pdf, name='convert_pdf'),
    path('download/<str:folder_name>/', views.download_images, name='download_images'),
]
