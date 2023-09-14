from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from retroapi.models import ControllerCollection, Owner, Controller, Condition


class ControllerCollectionView(ViewSet):

    def retrieve(self, request, pk):
        
        controller_collection = ControllerCollection.objects.get(pk=pk)
        serializer = ControllerCollectionSerializer(controller_collection)
        return Response(serializer.data)

    def list(self, request):

        controller_collections = ControllerCollection.objects.all()
        serializer = ControllerCollectionSerializer(controller_collections, many=True)
        return Response(serializer.data)

    def create(self, request):

        owner = Owner.objects.get(user=request.auth.user)
        controller = Controller.objects.get(pk=request.data["controller"])
        condition = Condition.objects.get(pk=request.data["condition"])

        controller_collection = ControllerCollection.objects.create(
            owner=owner,
            controller=controller,
            condition= condition,
        )

        serializer = ControllerCollectionSerializer(controller_collection)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        controller_collection = ControllerCollection.objects.get(pk=pk)
        controller_collection.condition = Condition.objects.get(pk=request.data["condition"])
        controller_collection.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        controller_collection = ControllerCollection.objects.get(pk=pk)
        controller_collection.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class OwnerControllerCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ('id', 'full_name')

class ControllerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Controller
        fields = ('id', 'name', 'releaseDate', 'description', 'img')

class ConditionControllerCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condition
        fields = ('id', 'label')

class ControllerCollectionSerializer(serializers.ModelSerializer):
    owner = OwnerControllerCollectionSerializer(many=False)
    controller = ControllerSerializer(many=False)
    condition = ConditionControllerCollectionSerializer(many=False)
    class Meta:
        model = ControllerCollection
        fields = ('id', 'owner', 'controller', 'condition')