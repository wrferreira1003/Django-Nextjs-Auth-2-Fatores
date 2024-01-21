from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
import firebase_admin
from firebase_admin import auth
from rest_framework import serializers
from .models import User
import uuid

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    #Chama a validação padrão primeiro
    def validate(self, attrs):
        data = super().validate(attrs)
        user = User.objects.get(username=attrs['username'])

        #Se o usuario tiver um numero de telefone, vamos gerar um codigo de verificacao
        if user.phone_number:
            try:
                phone_number = user.phone_number
                print(phone_number)
                # O Firebase envia o código de verificação para o número de telefone do usuário
                #verification_id = auth.(phone_number, app=None)
                #print(verification_id)

                #Gerando um identificado unico para essa sessao para controle do 2FA
                verification_session_id = str(uuid.uuid4())
                user.verification_session_id = verification_session_id
                user.save()

            except firebase_admin.exceptions.FirebaseError as e:
                raise serializers.ValidationError({'firebase_error': str(e)})
        else:
            raise serializers.ValidationError({'phone_number': 'Número de telefone não disponível'})

        return data
    
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