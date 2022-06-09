from django.urls import path
from . import views

app_name = 'notice'
urlpatterns = [
    path('', views.PostList.as_view(), name='index'),
    path('<int:pk>/', views.PostDetail.as_view(), name="detail"),
    path('category/<str:slug>/', views.category_page),
    path('tag/<str:slug>/', views.tag_page),
    # path('create_post/', views.PostCreate.as_view()),
    #path('update_post/<int:pk>/', views.PostUpdate.as_view()),
    path('update_post/<int:post_id>/',  views.postupdate, name="update_post"),
    path('create_post/', views.post, name="create_post"),
    path('search/<str:q>/', views.PostSearch.as_view()),
]
