from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from retroapi.models import Owner

class OwnerView(ViewSet):

    def retrieve(self, request, pk):
        owner = Owner.objects.get(pk=pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)

    def list(self, request):
        
        owners = Owner.objects.all()
        serializer = AuthorSerializer(owners, many=True)
        return Response(serializer.data)
    
class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Owner
        fields = ('id', 'user','full_name')