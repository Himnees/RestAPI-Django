
from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('stu/', views.RecordList.as_view()),
    path('stu/create', views.RecordCreate.as_view()),
    path('stu/update/<int:pk>/', views.RecordUpdate.as_view()),
    path('stu/retrieve/<int:pk>/', views.RecordRetrieve.as_view()),
    path('stu/delete/<int:pk>/', views.RecordDelete.as_view()),
    path('stu/ru/<int:pk>/', views.RecordRetrieveUpdate.as_view()),
    path('stu/rd/<int:pk>/', views.RecordRetrieveDelete.as_view()),
    path('stu/lc/', views.RecordListCreate.as_view()),

]
