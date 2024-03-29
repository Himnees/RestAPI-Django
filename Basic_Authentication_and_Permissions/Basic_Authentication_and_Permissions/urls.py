
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import RecordViewSet

router = DefaultRouter()

router.register('recordapi', RecordViewSet, basename='record' )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
