from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from retroapi.models import Game, Genre, Condition


class GameView(ViewSet):
    
    def retrieve(self, request, pk):

        game = Game.objects.get(pk=pk)
        serializer = GameSerializer(game)
        return Response(serializer.data)
    
    def list(self, request):

        game = Game.objects.all()
        serializer = GameSerializer(game, many=True)
        return Response(serializer.data)
    
    
    
    
    def destroy(self, request, pk):
        game = Game.objects.get(pk=pk)
        game.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class GenreGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id' ,'label')

class ConditionGameSerializier(serializers.ModelSerializer):
    class Meta:
        model = Condition
        fields = ('id', 'label')

class GameSerializer(serializers.ModelSerializer):
    genre = GenreGameSerializer(many=False)
    condition = ConditionGameSerializier(many=False)
    class Meta:
            model = Game
            fields = ('id','title','description', 'releaseDate', 'publisher', 'developer', 'modes', 'img', 'condition', 'genre')