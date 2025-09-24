from django.urls import path
from .views import post_api,comment_api,new_post

urlpatterns = [
    path("post_list/",post_api, name="post-api"),  
    path("yorum/<int:post_id>/",comment_api,name="comment-api"),
    path("new/",new_post,name='new-post'),
]