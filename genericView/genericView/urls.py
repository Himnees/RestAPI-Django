from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stu/<int:pk>/', views.RecordRUDView.as_view()),
    path('stu/', views.RecordCUview.as_view())
]
