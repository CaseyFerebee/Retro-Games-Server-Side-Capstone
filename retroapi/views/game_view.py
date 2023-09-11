from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from retroapi.models import Game


class GameView(ViewSet):
    
    def retrieve(self, request, pk):

        game = Game.objects.get(pk=pk)
        serializer = GameSerializer(game)
        return Response(serializer.data)
    
    def list(self, request):

        game = Game.objects.all()
        serializer = GameSerializer(game, many=True)
        return Response(serializer.data)
    
    
    
class GameSerializer(serializers.ModelSerializer):

    class Meta:
            model = Game
            fields = ('id','description', 'releaseDate', 'publisher', 'developer', 'modes', 'img', 'condition', 'genre')