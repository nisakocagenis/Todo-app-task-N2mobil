from django.urls import path
from .views import photo_api,album_api,new_photo

urlpatterns = [
    path("album_list/",album_api, name="album-api"),  
    path("foto/<int:album_id>/",photo_api,name="photo-api"),
    path("new/<int:album_id>/",new_photo,name='new-photo')
    
]