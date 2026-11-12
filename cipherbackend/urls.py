from django.contrib import admin
from django.urls import path, include
from cipher import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cipher.urls')),
    path('contact/', views.contact, name='contact'),
]
