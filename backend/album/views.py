from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Album,Photo
from .serializers import AlbumSerializer , PhotoSerializer
# Create your views here.
@api_view(['GET'])
def album_api(request):
    user = request.user
    album = Album.objects.filter(user=user).order_by('id')
    serializer = AlbumSerializer(album , many=True)
    return Response(serializer.data)

@api_view(['GET'])
def photo_api(request,album_id=None):
    photo = Photo.objects.filter(album_id=album_id).order_by('id')
    serializer = PhotoSerializer(photo, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def new_photo(request, album_id=None):
    user = request.user

    # POST => Yeni fotoğraf ekleme
    if request.method == 'POST':
        data = request.data.copy()
        photo = data.get('photo')


        data['album'] = album_id  # Albüm ID'sini ilişkilendir
        data['title'] = photo.name
        serializer = PhotoSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)

    # GET => Albüme ait fotoğrafları listeleme
    else:
        if not album_id:
            return Response({"error": "Album ID is required"}, status=400)

        photos = Photo.objects.filter(album_id=album_id)  # sadece bu albüme ait fotoğraflar
        serializer = PhotoSerializer(photos, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def new_album(request):
    user = request.user
    
    data =request.data
    if request.method == 'POST':

        data['user'] = user.id  
        serializer = AlbumSerializer(data=data)

        if serializer.is_valid():
            serializer.save(user=user)  
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)

    elif request.method == 'GET':
        albums = Album.objects.filter(user=user)  
        serializer = AlbumSerializer(albums, many=True)
        return Response(serializer.data, status=200)