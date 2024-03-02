"""View module for handling requests about LFG Post"""
from django.http import HttpResponseServerError
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from partyupapi.models import LFGPost, Games, User


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
        try:
            game_instance = Games.objects.get(pk=request.data["game"])
            user_instance = User.objects.get(pk=request.data["uuid"])
            lfgpost = LFGPost.objects.create(
                game=game_instance,
                title=request.data["title"],
                description=request.data["description"],
                needed_players=request.data["needed_players"],
                skill_level=request.data["skill_level"],
                platform=request.data["platform"],
                region=request.data["region"],
                mic_needed=request.data["mic_needed"],
                status=request.data["status"],
                uuid=user_instance,
                timestamp=request.data["timestamp"]
            )

            serializer = LFGPostSerializer(lfgpost)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk):
        """Handle PUT requests for posts"""
        post = LFGPost.objects.get(pk=pk)

        post.status = request.data.get("status", post.status)
        post.title = request.data.get("title", post.title)
        post.description = request.data.get("description", post.description)
        post.needed_players = request.data.get(
            "needed_players", post.needed_players)
        post.skill_level = request.data.get("skill_level", post.skill_level)
        post.platform = request.data.get("platform", post.platform)
        post.region = request.data.get("region", post.region)
        post.mic_needed = request.data.get("mic_needed", post.mic_needed)
        post.uuid = User.objects.get(pk=request.data.get("uuid", post.uuid.id))
        post.timestamp = request.data.get("timestamp", post.timestamp)
        post.game = Games.objects.get(
            pk=request.data.get("game", post.game.id))

        post.save()

        return Response({'message': 'Post updated successfully'}, status=status.HTTP_204_NO_CONTENT)

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
