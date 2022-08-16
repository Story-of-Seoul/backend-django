import email

from django.contrib.auth import authenticate

from .models import User, Profile
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.authtoken.models import Token #Token 모델
from rest_framework.validators import UniqueValidator #이메일 중복 방지를 위한 검증 도구


class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(
        write_only=True,
        required=True,
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
        )

        user.set_password(validated_data['password'])
        user.save()

        token = Token.objects.create(user=user)
        return user


class SignInSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user:
            token = Token.objects.get(user=user)
            return token
        raise serializers.ValidationError(
            {"error": "Unable to log in with provided credentials."}
        )
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('nickname','age', 'region', 'gender')

