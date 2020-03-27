from .serializers import UserSerializer, RegisterSerializer, LoginSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import permissions
from knox.models import AuthToken

class RegisterAPI(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        # serializer = self.get_serializer_class(data=request.data)
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            'user':UserSerializer(user,
            context=self.get_serializer()).data,
            'token':AuthToken.objects.create(user)[1]
        })
class LoginAPI(GenericAPIView):
    serializer_class = LoginSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            'user':UserSerializer(user,
            context=self.get_serializer_context()).data,
            'token': AuthToken.objects.create(user)[1]
        })
