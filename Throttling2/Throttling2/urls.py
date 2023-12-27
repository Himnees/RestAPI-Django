from django.contrib import admin
from django.urls import path, include
from api.views import RecordListView, RecordCreateView, RecordUpdateView, RecordRetrieveeView, RecordDestroyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RecordListView.as_view()),
    path('create/', RecordCreateView.as_view()),
    path('update/<int:pk>/', RecordUpdateView.as_view()),
    path('retrieve/<int:pk>/', RecordRetrieveeView.as_view()),
    path('delete/<int:pk>/', RecordDestroyView.as_view()),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]
