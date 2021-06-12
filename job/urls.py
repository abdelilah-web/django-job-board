from django.urls import path , include
from . import views
from . import api


app_name = 'job'
urlpatterns = [

    path('',views.job_list, name='job_list'), 
    path('add_job', views.add_job, name='add_job'),
    path('<str:slug>',views.job_detail , name= 'job_detail'),# the id of the job 

    ## api
    path('api/', api.job_list_api, name='job_list_api'),
    path('api/<int:id>/', api.job_detail_api, name='job_detail_api'),

    ## class based view
    path('v2/api/', api.JobListApi.as_view(), name='JobListApi'),
    path('v2/api/<int:id>/', api.JobDetailApi.as_view(), name='Job_Detail_Api'),        
]
