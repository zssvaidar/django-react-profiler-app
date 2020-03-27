from rest_framework.serializers import ModelSerializer, Serializer, HyperlinkedModelSerializer, SerializerMethodField
from rest_framework.relations import HyperlinkedIdentityField
from rest_framework import serializers
from ..models import User
from django.contrib.auth import authenticate

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'login', 'phonenumber', 'country', 'city')

class RegisterSerializer(ModelSerializer):
    # user_type = serializers.IntegerField(required=True)
    class Meta:
        model = User
        fields = ('id', 'login', 'password', 'phonenumber', 'country', 'city', 'user_type')
        extra_kwargs = {'password': {'write_only':True}}

    def create(self, validated_data):
        user = User.objects.create_user(
        validated_data['password'], validated_data['login'],
        validated_data['phonenumber'], validated_data['country'], validated_data['city'],
        validated_data['user_type'])
        return user
        
class LoginSerializer(Serializer):
    login = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user= authenticate(**data)
        if(user and user.is_active):
            return user
        raise serializers.ValidationError("validn error")
