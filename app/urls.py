from django.contrib import admin
from django.urls import path,include
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('gallery/', views.gallery, name='gallery'),
    path('about/', views.aboutus, name='about'),
    path('contact/', views.contactus, name='contact'),
    path('join/',views.join, name='join'),
    path('details/',views.details, name='details'),
    ]