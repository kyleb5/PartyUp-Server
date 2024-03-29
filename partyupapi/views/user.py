"""View module for handling requests about Users"""
from django.http import HttpResponseServerError
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from partyupapi.models import User


class UserView(ViewSet):
    """Party Up user view"""

    def retrieve(self, request, pk):
        """Handle GET requests for Users"""
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all users"""
        users = User.objects.all()

        fbkey = request.query_params.get('fbKey', None)

        if fbkey is not None:
            users = users.filter(fbKey=fbkey)

        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST users"""
        user = User.objects.create(
            joinDate=request.data["joinDate"],
            fbKey=request.data["fbKey"],
            account_discord=request.data["account_discord"],
            account_steam=request.data["account_steam"],
            account_xbox=request.data["account_xbox"],
            account_playstation=request.data["account_playstation"],
            username=request.data["username"]
        )
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for users"""
        user = User.objects.get(pk=pk)
        user.fbKey = request.data["fbKey"]
        user.joinDate = request.data["joinDate"]
        user.account_discord = request.data["account_discord"]
        user.account_steam = request.data["account_steam"]
        user.account_xbox = request.data["account_xbox"]
        user.account_playstation = request.data["account_playstation"]
        user.id = request.data["id"]
        user.username = request.data["username"]
        user.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """Handle DELETE users"""
        user = User.objects.get(pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for user"""
    class Meta:
        model = User
        fields = ('fbKey', 'joinDate', 'id', 'account_playstation',
                  'account_xbox', 'account_steam', 'account_discord', 'email_address', 'username')
