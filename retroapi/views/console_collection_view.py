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

    def list(self, request):

        console_collections = ConsoleCollection.objects.all()
        serializer = ConsoleCollectionSerializer(console_collections, many=True)
        return Response(serializer.data)

    def create(self, request):

        owner = Owner.objects.get(user=request.auth.user)
        console = Console.objects.get(pk=request.data["console"])
        condition = Condition.objects.get(pk=request.data["condition"])

        console_collection = ConsoleCollection.objects.create(
            owner=owner,
            console=console,
            condition= condition,
        )

        serializer = ConsoleCollectionSerializer(console_collection)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        console_collection = ConsoleCollection.objects.get(pk=pk)
        console_collection.condition = Condition.objects.get(pk=request.data["condition"])
        console_collection.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        console_collection = ConsoleCollection.objects.get(pk=pk)
        console_collection.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class OwnerConsoleCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ('id', 'full_name')

class ConsoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Console
        fields = ('id', 'name', 'releaseDate', 'description', 'img')

class ConditionConsoleCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condition
        fields = ('id', 'label')

class ConsoleCollectionSerializer(serializers.ModelSerializer):
    owner = OwnerConsoleCollectionSerializer(many=False)
    console = ConsoleSerializer(many=False)
    condition = ConditionConsoleCollectionSerializer(many=False)
    class Meta:
        model = ConsoleCollection
        fields = ('id', 'owner', 'console', 'condition')