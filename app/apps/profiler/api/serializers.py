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
#
#
# class ProfileSerializer(HyperlinkedModelSerializer):
#
#     url = HyperlinkedIdentityField(
#         view_name='profiler-gc:profiler',
#         lookup_field='pk'
#     )
#     ids = SerializerMethodField()
#
#     class Meta:
#         model = profile
#         fields = ['url','id', 'ids', 'name', 'surname', 'phone_number', 'mail', 'address']
#
#     def get_ids(self, obj):
#         return obj.id
