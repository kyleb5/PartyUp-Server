"""View module for handling requests about LFG Post"""
from django.http import HttpResponseServerError
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from partyupapi.models import LFGPost, Games


class LFGPostView(ViewSet):
    """Party Up Post View"""

    def retrieve(self, request, pk):
        """Handle GET requests for posts1"""
        try:
            lfgpost = LFGPost.objects.get(pk=pk)
            serializer = LFGPostSerializer(lfgpost)
            return Response(serializer.data)
        except LFGPost.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get ALL posts or posts for a specific game"""
        lfgpost = LFGPost.objects.all()

        gameid = request.query_params.get('game', None)

        if gameid is not None:
            lfgpost = lfgpost.filter(game__id=gameid)

        serializer = LFGPostSerializer(lfgpost, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST for posts"""
        games = Games.objects.get(pk=request.data["games"])
        lfgpost = LFGPost.objects.create(
            games=request.data["games"],
            title=request.data["title"],
            description=request.data["description"],
            needed_players=request.data["needed_players"],
            skill_level=request.data["skill_level"],
            platform=request.data["platform"],
            region=request.data["region"],
            mic_needed=request.data["mic_needed"],
            status=request.data["status"],
            uuid=request.data["uuid"],
            timestamp=request.data["timestamp"]
        )

    def update(self, request, pk):
        """Handle PUT requests for posts"""
        post = LFGPost.objects.get(pk=pk)
        post.games = request.data["games"]
        post.title = request.data["title"]
        post.description = request.data["description"]
        post.needed_players = request.data["needed_players"]
        post.skill_level = request.data["skill_level"]
        post.platform = request.data["platform"]
        post.region = request.data["region"]
        post.mic_needed = request.data["mic_needed"]
        post.status = request.data["status"]
        post.uuid = request.data["uuid"]
        post.timestamp = request.data["timestamp"]
        post.save()

        return Response({'message': 'Post updated succesfully'}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """Handle DELETE requests for LFG Post"""
        post = LFGPost.objects.get(pk=pk)
        post.delete()
        return Response({'message': 'Post deleted'}, status=status.HTTP_204_NO_CONTENT)


class LFGPostSerializer(serializers.ModelSerializer):
    """JSON serializer for lfg post"""
    class Meta:
        model = LFGPost
        fields = ('id', 'game', 'title', 'description', 'needed_players',
                  'skill_level', 'platform', 'region', 'mic_needed', 'status', 'uuid', 'timestamp')
        depth = 1
