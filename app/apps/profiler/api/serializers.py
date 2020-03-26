from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer, SerializerMethodField
from rest_framework.relations import HyperlinkedIdentityField
from ..models import service, User

# class ProfileSerializer(ModelSerializer):

class ServiceSerializer(HyperlinkedModelSerializer):

    url = HyperlinkedIdentityField(
        view_name='profiler_service:service',
        lookup_field='pk'
    )
    class Meta:
        model = service
        fields = ['url', 'id',  'description', 'price']

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'login', 'phonenumber', 'country', 'city')
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['login'], validated_data['phonenumber'],
        validated_data['country'], validated_data['city'], validated_data['password'])
        return user
