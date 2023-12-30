from django.contrib import admin
from django.urls import path, include
from api.views import SingerViewset, SongViewset
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register('songapi', SongViewset, basename='song')
router.register('singerapi', SingerViewset, basename='singer')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

