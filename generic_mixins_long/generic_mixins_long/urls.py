
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('listapi/', views.RecordListView.as_view()),
    path('Creatapi/', views.RecordCreateView.as_view()),
    path('retrive/<int:pk>/', views.RecordRetriveView.as_view()),
    path('update/<int:pk>/', views.RecordUpdateView.as_view()),
    path('destroy/<int:pk>/',views.RecordDeleteView.as_view()),
    
]
