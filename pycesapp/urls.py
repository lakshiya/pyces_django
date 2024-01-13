from django.urls import path
from .views import file_upload, file_upload_success, file_upload_failure

urlpatterns = [
    path('', file_upload, name='file_upload'),
    path('success/', file_upload_success, name='file_upload_success'),
    path('failure/', file_upload_failure, name='file_upload_failure')
]
