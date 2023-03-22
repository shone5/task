from django.urls import path
from Myapp import views

urlpatterns = [
    path('', views.upload_csv, name='upload_csv'),


]
