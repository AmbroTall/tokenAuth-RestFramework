from django.urls import path
from .views import api_view_delete,api_view_create,api_view_update,api_view_detail,BlogApiListView


urlpatterns = [
    path('posts/<str:slug>', api_view_detail, name='detailview'),
    path('posts/update/<str:slug>', api_view_update, name='updateview'),
    path('posts/delete/<str:slug>', api_view_delete, name='deleteview'),
    path('create/', api_view_create, name='createview'),
    path('all/blogs/', BlogApiListView.as_view(), name='listView'),
]

