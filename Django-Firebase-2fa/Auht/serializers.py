from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.core.mail import send_mail
import random
import string
from rest_framework import serializers
from .models import User, GerenciadorSystem

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    #Chama a validação padrão primeiro
    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user # O usuário autenticado

        # Gerar um código de verificação
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        
        # Salvar o código temporariamente (pode ser no próprio modelo de usuário ou em cache)
        GerenciadorSystem.objects.create(user=user, code=code)

        print(user.email)
        # Enviar o código via e-mail
        send_mail(
            'Seu código de verificação',
            f'Seu código de verificação é: {code}',
            'teste@wrweb.net.br',  # Endereço de e-mail de envio
            [user.email],  # Endereço de e-mail do destinatário
            fail_silently=False,
        )

        # Retorne uma resposta personalizada
        return {
            "message": "Código de verificação enviado. Por favor, verifique seu e-mail.",
            "user_id": user.id,  # ID do usuário para referência futura
            "username": user.username  # Nome de usuário para identificação   
        }
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user