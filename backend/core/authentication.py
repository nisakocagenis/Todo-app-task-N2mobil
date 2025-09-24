
from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions
from rest_framework.authtoken.models import Token

class CustomAuth(authentication.BaseAuthentication):
    def authenticate(self, request):
        token_key = request.META.get('HTTP_AUTHORIZATION')
        if not token_key:
            raise exceptions.NotAuthenticated('Token bulunamadı')
        
        token = Token.objects.get(key=token_key.split(" ")[1])

        if not token:
            raise exceptions.NotAuthenticated("Token geçersiz.")
        
        if not token.user.is_staff:
            raise exceptions.NotAuthenticated("Kullanıcının sisteme giriş yetkisi yok.")


        return (token.user, None)
    
