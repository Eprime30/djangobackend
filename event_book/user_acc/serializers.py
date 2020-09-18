
from rest_framework import serializers
from .models import Account
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
import re


class RegisterSerializer(serializers.ModelSerializer):

    confirm_password = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'email', 'password',
                  'confirm_password', 'username',  'phone', 'address']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')
        password = attrs.get('password', '')
        confirm_password = attrs.get('confirm_password', '')
        phone = attrs.get('phone', '')

        if password != confirm_password:
            raise serializers.ValidationError(
                {'password': 'Password must match.'})

        if not username.isalnum():
            raise serializers.ValidationError(
                'The username should only contain alphanumeric characters')

        if re.findall('[A-Z, a-z]', phone):
            raise serializers.ValidationError(
                'The phone should only contain numeric characters')

        if not re.findall('\d', password):
            raise serializers.ValidationError(
                "The password must contain at least 1 digit, 0-9.")
        return attrs

    def create(self, validated_data):
        return Account.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)
    username = serializers.CharField(
        max_length=255, min_length=3, read_only=True)
    tokens = serializers.CharField(max_length=68, min_length=6, read_only=True)

    class Meta:
        model = Account
        fields = ['email', 'password', 'username', 'tokens']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')

        user = auth.authenticate(email=email, password=password)
        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        if not user.is_active:
            raise AuthenticationFailed('Account disabled, contact admin')

        return {
            'email': user.email,
            'username': user.username,
            'tokens': user.tokens()
        }

        return super().validate(attrs)
