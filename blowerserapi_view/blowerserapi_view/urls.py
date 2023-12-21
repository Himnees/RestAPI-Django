from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', views.RecordApi),
    path('studentapi/<int:pk>/', views.RecordAPI)
]
