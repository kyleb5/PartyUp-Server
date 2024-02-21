from django.http import HttpResponseServerError
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from partyupapi.models import LFGPost, User, LFGGroupMember


class LFGGroupMemberView(ViewSet):
    """Party Up Group Member"""

    def retrieve(self, request, pk):
        """Handle GET requests"""
        try:
            lfggroupmembers = LFGGroupMember.objects.get(pk=pk)
            serializer = LFGGroupMemberSerializer(lfggroupmembers)
            return Response(serializer.data)
        except LFGGroupMember.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle Get requests for ALL group members"""
        groupmember = LFGGroupMember.objects.all()
        serializer = LFGGroupMemberSerializer(groupmember, many=True)
        return Response(serializer.data)

    def destroy(self, request, pk):
        """Handle DELETE request"""
        groupmember = LFGGroupMember.objects.get(pk=pk)
        groupmember.delete()
        return Response({'message': 'Member deleted from group'}, status=status.HTTP_204_NO_CONTENT)

    def create(self, request):
        """Handle POST for group members"""
        user = User.objects.get(pk=request.data["user"])
        post = LFGPost.objects.get(pk=request.data["post"])
        groupmember = LFGGroupMember.objects.create(
            user=user,
            post=post
        )
        serializer = LFGGroupMemberSerializer(groupmember)
        return Response(serializer.data)


class LFGGroupMemberSerializer(serializers.ModelSerializer):
    """JSON serializer for lfg group member"""
    class Meta:
        model = LFGGroupMember
        fields = ('id', 'user', 'post')
        depth = 1
