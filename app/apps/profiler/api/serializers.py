from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer, SerializerMethodField
from rest_framework.relations import HyperlinkedIdentityField
from ..models import service

# class ProfileSerializer(ModelSerializer):

class ServiceSerializer(HyperlinkedModelSerializer):

    url = HyperlinkedIdentityField(
        view_name='profiler_service:service',
        lookup_field='pk'
    )
    class Meta:
        model = service
        fields = ['url', 'id',  'description', 'price']
