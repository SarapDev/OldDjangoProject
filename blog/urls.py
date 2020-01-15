from django.urls import path

from .views import *

urlpatterns = [
    path('', posts_list, name='posts_list_url'),
    path('post/create/', PostCreate.as_view(), name='post_create_url'),
    path('post/<str:slug>/', PostDetail.as_view(), name='post_detail_url'),
    path('post/<str:slug>/change/', PostChange.as_view() , name='post_change_url'),
    path('post/<str:slug>/delete/', PostDelete.as_view() , name='post_delete_url'),
    path('tags/', tags_list, name='tags_list_url'),
    path('tag/create/', TagCreate.as_view(), name='tag_create_url'),
    path('tag/<str:slug>/', TagDetail.as_view(), name='tag_detail_url'),
    path('tag/<str:slug>/change/', TagChange.as_view(), name='tag_change_url'),
    path('tag/<str:slug>/delete/', TagDelete.as_view(), name='tag_delete_url')
]