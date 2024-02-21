from rest_framework.decorators import api_view
from rest_framework.response import Response
from partyupapi.models import User


@api_view(['POST'])
def check_user(request):
    '''Checks to see if User has Associated User Account

    Method arguments:
      request -- The full HTTP request object
    '''
    fbKey = request.data['fbKey']

    # Use the built-in authenticate method to verify
    # authenticate returns the user object or None if no user is found
    user = User.objects.filter(fbKey=fbKey).first()

    # If authentication was successful, respond with their token
    if user is not None:
        data = {
            'id': user.id,
            'joinDate': user.joinDate,
            'fbKey': user.fbKey,
            'account_playstation': user.account_playstation,
            'account_xbox': user.account_xbox,
            'account_steam': user.account_steam,
            'account_discord': user.account_discord
        }
        return Response(data)
    else:
        # Bad login details were provided. So we can't log the user in.
        data = {'valid': False}
        return Response(data)


@api_view(['POST'])
def register_user(request):
    '''Handles the creation of a new user for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

    user = User.objects.create(
        joinDate=request.data["joinDate"],
        fbKey=request.data["fbKey"],
        account_playstation=request.data["account_playstation"],
        account_xbox=request.data["account_xbox"],
        account_steam=request.data["account_steam"],
        account_discord=request.data["account_discord"]
    )

    # Return the user info to the client
    data = {
        'id': user.id,
        'joinDate': user.joinDate,
        'fbKey': user.fbKey,
        'account_playstation': user.account_playstation,
        'account_xbox': user.account_xbox,
        'account_steam': user.account_steam,
        'account_discord': user.account_discord
    }
    return Response(data)
