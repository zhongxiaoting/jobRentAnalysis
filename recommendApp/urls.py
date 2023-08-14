# coding=utf-8

from django.urls import path

from . import views

app_name = 'recommendApp'
urlpatterns = [
    path('job_list/', views.job_lists, name='job_list'),
    path('house_list/', views.house_lists, name='house_list'),
    path('job_search/', views.job_search, name='job_search'),
    path('house_search/', views.house_search, name='house_search'),
    path('house_recommand/', views.house_recommand, name='house_recommand'),
    path('update', views.update_job_house, name='update_job_house'),
    path('jisuan', views.jisuan, name='jisuan'),

]