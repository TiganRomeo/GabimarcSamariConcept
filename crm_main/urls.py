from django.contrib import admin
from django.urls import path
from excavator import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('excavators/', views.excavators, name='excavators'),
    path('prices/', views.prices, name='prices'),
    path('contact/', views.contact, name='contact'),
]