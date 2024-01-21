from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics, permissions, views, status
from .serializers import MyTokenObtainPairSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from .models import User, GerenciadorSystem

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,) #Permite que qualquer um se registre

class CodeView(views.APIView):
    permission_classes = (permissions.AllowAny,) #Permite que qualquer um verifique o código

    def post(self, request, *arg, **kwargs):
        username = request.data.get('username')
        code = request.data.get('code')

        # Verificar se o código está correto
        try:
            user = User.objects.get(username=username)
            verification_code = GerenciadorSystem.objects.filter(user=user, code=code).latest('created_at')

            if verification_code.is_expired:
                return Response({'message': 'Código expirado.'}, status=status.HTTP_400_BAD_REQUEST)
            if verification_code.code != code:
                return Response({'message': 'Código incorreto.'}, status=status.HTTP_400_BAD_REQUEST)
                
            #Gerar um novo token de atualização
            refresh = RefreshToken.for_user(user)
            return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'user': user.username
                })
            
        except User.DoesNotExist:
            return Response({'message': 'Usuário não encontrado.'}, status=status.HTTP_404_NOT_FOUND)