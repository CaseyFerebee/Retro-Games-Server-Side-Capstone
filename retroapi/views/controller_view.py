from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from retroapi.models import Controller


class ControllerView(ViewSet):

    def retrieve(self, request, pk):
        
        controller = Controller.objects.get(pk=pk)
        serializer = ControllerSerializer(controller)
        return Response(serializer.data)

    def list(self, request):

        controllers = Controller.objects.all()
        serializer = ControllerSerializer(controllers, many=True)
        return Response(serializer.data)

class ControllerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Controller
        fields = ('id', 'name', 'releaseDate', 'description', 'img')