from django.urls import path
from . import views


urlpatterns = [
    path('upload/', views.upload_course, name='upload_course'),
    path('course/<int:pk>/', views.course_detail, name='course_detail'),
    path('', views.Homepage.as_view(), name='Homepage'),
    path('search/', views.SearchResults.as_view(), name='Search_results'),

]