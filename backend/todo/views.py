
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer
from django.shortcuts import get_object_or_404


@api_view(['GET'])
def todo_api(request):
    user = request.user
    todos = Todo.objects.filter(user=user).order_by('id')
    serializers = TodoSerializer(todos , many = True)
    return Response(serializers.data)

@api_view(['GET', 'PATCH'])
def todo_patch(request, pk=None):
    if pk:  
        todo = get_object_or_404(Todo, pk=pk)
        if request.method == 'PATCH':
            serializer = TodoSerializer(todo, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        serializer = TodoSerializer(todo)
        return Response(serializer.data)
    else: 
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)
    
@api_view(['GET','POST'])
def new_todo(request):
    user = request.user
    if request.method == 'POST':
        data = request.data.copy()   
        data['user'] = user.id  
        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    else:  
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)
    