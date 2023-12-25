
from django.contrib import admin
from django.urls import path, include
from api.views import RecordViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
routers = DefaultRouter()
routers.register('studentapi', RecordViewSet, basename='record')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(routers.urls)),
    # path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('gettoken/', obtain_auth_token)
]
