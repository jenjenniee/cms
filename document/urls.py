from django.urls import path
from . import views
from .views import *

app_name = 'document'
urlpatterns = [
    path('', views.main, name="document-main"),
    path('daily/write', ReportWrite.as_view(), name="document-report-write"),
    path('daily/read/<pk>', ReportRead.as_view(), name="document-report-read"),
    path("userlist", views.ajax_userlist, name="document-ajax-userlist")
]
