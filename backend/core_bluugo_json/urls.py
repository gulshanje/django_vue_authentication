from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_view_json, name='upload_view_json'),

]