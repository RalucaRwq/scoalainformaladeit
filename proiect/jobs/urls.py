from django.urls import path
from jobs import views

app_name = 'jobs'

urlpatterns = [
    path('add_job/', views.CreateJobView.as_view(), name='add'),
    path('<int:pk>/update_job/', views.UpdateJobView.as_view(), name='update'),
    path('list/', views.ListJobView.as_view(), name='list'),
    path('delete/<int:pk>/', views.delete_job, name='remove')
    ]
