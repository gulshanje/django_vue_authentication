from django.urls import path, include
from .views import upload_file_view
app_name = 'CSVs'
urlpatterns = [
    path('', upload_file_view, name='upload-view'),
    
]