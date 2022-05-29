from django.urls import path
from board import views
app_name='board'

urlpatterns=[
#게시판
    path('Viewboard/',views.Viewboard,name="Viewboard"),
    path('Writeboard/',views.Writeboard,name="Writeboard"),
    path('Viewboard/Boarddetail/<int:pk>',views.Boarddetail,name="Boarddetail"),
    path('Viewboard/Boarddetail/Deleteboard/<int:pk>',views.Deleteboard, name="Deleteboard"),
    path('Viewboard/Boarddetail/Editboard/<int:pk>',views.Editboard, name="Editboard")
]