
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stu/<int:pk>', views.APIView),
    path('stu/', views.APIViewall),
]
