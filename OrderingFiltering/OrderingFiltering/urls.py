from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from api.views import RecordViewSet

# router = DefaultRouter()
# router.register('recordapi', RecordViewSet, basename='record')

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include(router.urls)),
    path('', RecordViewSet.as_view()),
    path('auth/', include('rest_framework.urls',namespace='rest_framework')),
]