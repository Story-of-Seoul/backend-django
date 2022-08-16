import email
from .models import User
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate
from django.core.mail import EmailMessage
from rest_framework import serializers
from rest_framework.authtoken.models import Token #Token 모델
from rest_framework.validators import UniqueValidator #이메일 중복 방지를 위한 검증 도구

class RegisterSerializer(serializers.ModelSerializer): #회원가입 시리얼라이저
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())], #이메일 중복검증
        )
    password = serializers.CharField(
        write_only = True,
        required = True,
        validators = [validate_password], #비밀번호 검증
    )
    password2 = serializers.CharField(write_only=True, required=True) #비밀번호 확인 필드
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())], 
        required=True
    )
    age = serializers.IntegerField(required=True)
    region = serializers.CharField(max_length=45)
    gender = serializers.CharField(required=True)
    
    
    class Meta:
        model = User
        fields = ('email', 'password', 'password2','username', 'age', 'region', 'gender')
        
    def validate(self, data): #비밀번호 일치 여부 확인
        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                {"password":"Password fields didn't match."}
            )
        return data
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
            age = validated_data['age'],
            region = validated_data['region'],
            gender = validated_data['gender'],
        )
        
        user.set_password(validated_data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return user
    
    
class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)
        
    def validate(self, data):
        user = authenticate(**data)
        if user:
            token = Token.objects.get(user=user)
            return token
        raise serializers.ValidationError(
            {"error":"Unable to log in with provided credentials."}
        )