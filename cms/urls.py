from django.urls import path,include
from . import views

app_name='cms'
urlpatterns = [
    path('', views.index, name='index'),
    
]