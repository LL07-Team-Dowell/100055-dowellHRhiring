from django.urls import path

from .views import application_view, get_jobs, add_new_job, get_applications, candindateview
# from .views import UpdateaACStatus,
from .views import hrview, update_job, delete_job
urlpatterns = [
    path('add_job/', add_new_job, name='add_new_job'),
    path('get_jobs/', get_jobs, name='get_jobs'),
    path('get_applications/', get_applications, name="get_applications"),
    path('candindateview/', candindateview, name="candindateview"),
    path('application_view/', application_view, name='application_view'),
    path('hrview/', hrview, name="hrview"),
    path('update_job/', update_job, name="update_job"),
    path('delete_job/', delete_job, name="delete_job"),
]
