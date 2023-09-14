from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from retroapi.models import GameCollection, Owner, Game, Condition


class GameCollectionView(ViewSet):

    def retrieve(self, request, pk):
        
        game_collection = GameCollection.objects.get(pk=pk)
        serializer = GameCollectionSerializer(game_collection)
        return Response(serializer.data)

    def list(self, request):

        game_collections = GameCollection.objects.all()
        serializer = GameCollectionSerializer(game_collections, many=True)
        return Response(serializer.data)

    def create(self, request):

        owner = Owner.objects.get(user=request.auth.user)
        game = Game.objects.get(pk=request.data["game"])
        condition = Condition.objects.get(pk=request.data["condition"])

        game_collection = GameCollection.objects.create(
            owner=owner,
            game=game,
            condition= condition,
        )

        serializer = GameCollectionSerializer(game_collection)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        game_collection = GameCollection.objects.get(pk=pk)
        game_collection.condition = Condition.objects.get(pk=request.data["condition"])
        game_collection.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        game_collection = GameCollection.objects.get(pk=pk)
        game_collection.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class OwnerGameCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ('id', 'full_name')

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'title', 'description', 'releaseDate', 'publisher', 'developer', 'modes', 'img', 'genre')

class ConditionGameCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condition
        fields = ('id', 'label')

class GameCollectionSerializer(serializers.ModelSerializer):
    owner = OwnerGameCollectionSerializer(many=False)
    game = GameSerializer(many=False)
    condition = ConditionGameCollectionSerializer(many=False)
    class Meta:
        model = GameCollection
        fields = ('id', 'owner', 'game', 'condition')