"""View module for handling requests about Games"""
from django.http import HttpResponseServerError
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from partyupapi.models import Games


class GamesView(ViewSet):
    """Games View"""

    def retrieve(self, request, pk):
        """Handle GET requests fort Games"""
        try:
            games = Games.objects.get(pk=pk)
            serializer = GamesSerializer(games)
            return Response(serializer.data)
        except Games.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Hnadle GET requests to get all games"""
        games = Games.objects.all()
        serializer = GamesSerializer(games, many=True)
        return Response(serializer.data)


class GamesSerializer(serializers.ModelSerializer):
    """JSON serializer for games"""
    class Meta:
        model = Games
        fields = ('id', 'name', 'cover_image')
