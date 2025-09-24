
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.contrib.auth import authenticate
from rest_framework import status
from .serializers import UserSerializer,CompanySerializer,AddressSerializer
from .models import Company,Address
from core.authentication import CustomAuth



@api_view(['GET'])
def home_api(request):
    print('--->', request.user)
    data = {"message": "Merhaba korall!"}
    return Response(data)


# @api_view(["POST"])
# def login_view(request):
#     username = request.data.get("username")
#     password = request.data.get("password")

#     user = authenticate(username=username, password=password)

#     if user is not None:
#         return Response({"success": True, "message": "Login başarılı!"})
#     else:
#         return Response(
#             {"success": False, "message": "Kullanıcı adı veya şifre yanlış!"},
#             status=status.HTTP_401_UNAUTHORIZED
#         )
    
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def example_view(request, format=None):
    content = {
        'status': 'request was permitted'
    }
    return Response(content)

from rest_framework.authtoken.models import Token

@api_view(["POST"])
@permission_classes([AllowAny])
@authentication_classes([])
def login_view(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)

    if user is not None:
        # Token üretelim
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            "success": True,
            "message": "Login başarılı!",
            "token": token.key,
            "user": UserSerializer(user).data
        })

    else:
        return Response(
            {"success": False, "message": "Kullanıcı adı veya şifre yanlış!"},
            status=status.HTTP_401_UNAUTHORIZED
        )

from .models import User

@api_view(['GET'])
def all_users(request):
    user = User.objects.all()
    serializer = UserSerializer(user, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def company_api(request):
    company = Company.objects.all()
    serializers = CompanySerializer(company , many = True)
    return Response(serializers.data)

@api_view(['GET'])
def address_api(request):
    address = Address.objects.all()
    serializers = AddressSerializer(address , many = True)
    return Response(serializers.data)

@api_view(['GET'])
def photo_api(request):
    user_photo = User.objects.all()

