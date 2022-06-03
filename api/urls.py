from django.urls import path,include
from . import views


urlpatterns = [
    path('plan/', views.PlanAPI.as_view())
]