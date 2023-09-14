from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from retroapi.models import Game, Genre, Owner



class GameView(ViewSet):
    
    def retrieve(self, request, pk):

        game = Game.objects.get(pk=pk)
        serializer = GameSerializer(game)
        return Response(serializer.data)

    def list(self, request):

        games = Game.objects.all()
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)

class GenreGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id' ,'label')

class GameSerializer(serializers.ModelSerializer):
    genre = GenreGameSerializer(many=False)
    class Meta:
            model = Game
            fields = ('id','title','description', 'releaseDate', 'publisher', 'developer', 'modes', 'img','genre')