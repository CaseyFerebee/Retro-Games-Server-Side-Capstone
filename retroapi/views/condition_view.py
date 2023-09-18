from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from retroapi.models import Condition


class ConditionView(ViewSet):

    def retrieve(self, request, pk):
        
        condition = Condition.objects.get(pk=pk)
        serializer = ConditionSerializer(condition)
        return Response(serializer.data)

    def list(self, request):

        conditions = Condition.objects.all()
        serializer = ConditionSerializer(conditions, many=True)
        return Response(serializer.data)


class ConditionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Condition
        fields = ('id', 'label')