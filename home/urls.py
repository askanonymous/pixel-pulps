from django.urls import path
from home import views
from django.contrib import admin

urlpatterns = [
    path("", views.index, name='home'),
   path('total-records/', views.total_records, name='total_records'),
   path('mean-salary/', views.mean_salary, name='mean_salary'),
   path('median-salary/', views.median_salary, name='median_salary')
   path('percentile-25/', views.percentile_25, name='percentile_25'),
    path('percentile-75/', views.percentile_75, name='percentile_75'),
]
