# coding=utf-8

from django.urls import path

from . import views

app_name = 'navigationApp'
urlpatterns = [
    path('job_house_list/<int:id>/', views.job_house_list, name='job_house_list'),
    # path('job_list/', views.job_lists, name='job_list'),


]