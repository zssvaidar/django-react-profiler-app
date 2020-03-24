from rest_framework.generics import ListAPIView
from rest_framework.renderers import TemplateHTMLRenderer
from ..models import service
from .serializers import ServiceSerializer
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from django.http import Http404
from rest_framework.response import Response
import datetime

class ServiceListView(ListAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    queryset = service.objects.all()
    serializer_class = ServiceSerializer
    template_name = 'service/services.html'

    def get(self, request):
        queryset = service.objects.all()
        serializer_class = ServiceSerializer(queryset, many=True, context={'request':request})
        print(serializer_class.data)
        return Response({'services': serializer_class.data})

    def post(self, request, format=None):
        serializer_class = ServiceSerializer(data=request.data, context={'request': request})
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data)

        return Response(serializer.errors)

class ServiceView(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'service/service.html'

    def get(self, request, pk, format=None):
        self.pk=pk
        queryset = self.get_object()
        serializer_class = ServiceSerializer(queryset,  context={'request':request})
        return Response({'service':serializer_class.data, 'date':datetime.datetime.now().strftime("%Y-%m-%d %H:%M")})

    def put(self, request, pk, format=None):
        self.pk = pk
        queryset = self.get_object()
        serializer_class = ServiceSerializer(queryset, data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response({'services':serializer_class.data})
        return Response(serializer_class.errors)

    def delete(self, request, pk, format=None):
        self.pk=pk
        snippet = self.get_object()
        snippet.delete()
        return Response()

    def get_object(self):
        try:
            return service.objects.get(id=self.pk)
        except service.DoesNotExist:
            raise Http404
        return
