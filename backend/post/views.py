from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post,Comment
from .serializers import PostSerializer , CommentSerializer

# Create your views here.
@api_view(['GET'])
def post_api(request):
    user = request.user
    post = Post.objects.filter(user=user).order_by('id')
    serializers = PostSerializer(post , many = True)
    return Response(serializers.data)

@api_view(['GET'])
def comment_api(request , post_id=None):
    comment = Comment.objects.filter(post_id=post_id).order_by('id')
    serializers = CommentSerializer(comment, many = True)
    return Response(serializers.data)


@api_view(['GET'])
def photo_api(request):
    comment_photo = Comment.objects.all()

@api_view(['GET','POST'])
def new_post(request):
    user = request.user
    if request.method == 'POST':
        data = request.data.copy()   
        data['user'] = user.id  
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    else:  
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)