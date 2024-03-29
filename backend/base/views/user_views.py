from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status

from rest_framework.response import Response

from base.models import *
from base.serializers import  UserSerializer, UserSerialiazerWithToken


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerialiazerWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v

        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    user = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateUserProfile(request):
    print('userupdate View')
    user = request.data
    serializer = UserSerialiazerWithToken(user, many=True)

    data = request.data
    user.first_name = data['name']
    user.username = data['email']
    user.email = data['email']
    if data['password'] != '':
        user.password = make_password(data['password'])

    user.save()
    return Response(serializer.data)

@api_view(['POST'])
# @permission_classes([IsAdminUser])
def registerUser(request):
    data =request.data
    try:
        user = User.objects.create(
            first_name = data['name'],
            username=data['email'],
            email=data['email'],
            password=make_password(data['password'])
        )
        serializer = UserSerialiazerWithToken(user, many=False)
    except:
        message = {'default': 'email alredy exists'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.data)
