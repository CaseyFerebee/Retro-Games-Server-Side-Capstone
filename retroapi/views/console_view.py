from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from retroapi.models import Console


class ConsoleView(ViewSet):

    def retrieve(self, request, pk):
        
        console = Console.objects.get(pk=pk)
        serializer = ConsoleSerializer(console)
        return Response(serializer.data)

    def list(self, request):

        consoles = Console.objects.all()
        serializer = ConsoleSerializer(consoles, many=True)
        return Response(serializer.data)


class ConsoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Console
        fields = ('id', 'name', 'releaseDate', 'description', 'img')