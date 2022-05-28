from django.urls import path,include
from . import views

app_name='commute'
urlpatterns = [
    path('home/',views.commute_home,name="commute_home"),
    path('attendance/',views.attendance,name="attendance"),
    path('offwork',views.off_work,name="off_work"),
    path('home_attendance/',views.home_attendance,name="home_attendance"),
    path('home_offwork',views.home_off_work,name="home_off_work"),

]