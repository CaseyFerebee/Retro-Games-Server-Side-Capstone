from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from retroapi.models import ConsoleCollection, Owner, Console, Condition


class ConsoleCollectionView(ViewSet):

    def retrieve(self, request, pk):
        
        console_collection = ConsoleCollection.objects.get(pk=pk)
        serializer = ConsoleCollectionSerializer(console_collection)
        return Response(serializer.data)



class OwnerCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ('full_name' ,)

class ConsoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Console
        fields = ('id', 'name', 'releaseDate', 'description', 'img')


class ConditionConsoleCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condition
        fields = ('id', 'label')

class ConsoleCollectionSerializer(serializers.ModelSerializer):
    owner = OwnerCollectionSerializer(many=False)
    condition = ConditionConsoleCollectionSerializer(many=False)
    console = ConsoleSerializer(many=False)
    class Meta:
        model = ConsoleCollection
        fields = ('id', 'owner', 'console', 'condition')