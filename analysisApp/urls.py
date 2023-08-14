# coding=utf-8

from django.urls import path

from . import views

app_name = 'analysisApp'
urlpatterns = [
    path('job_analysis', views.job_analysis, name='job_analysis'),
    path('house_analysis', views.house_analysis, name='house_analysis'),
    path('job_distance', views.job_distance, name='job_distance'),


]