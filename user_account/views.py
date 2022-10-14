from django.contrib.auth import logout
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from user_account.models import RestaurantUser
from user_account.serializers import UserRegistrationSerializers, UserUpdateSerializers, UserPasswordChangeSerializers


class UserRegistrationView(APIView):
    @staticmethod
    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'username': openapi.Schema(type=openapi.TYPE_STRING, title='Username', example='username'),
            'password': openapi.Schema(type=openapi.TYPE_STRING, title='Password', example='123@abc'),
            'email': openapi.Schema(type=openapi.TYPE_STRING, title='Email Address', example='user@example.com'),
            'phone_number': openapi.Schema(type=openapi.TYPE_STRING, title='Phone Number', example='+8801XXXXXXXXX')
        }
    ))
    def post(request, *args, **kwargs):
        serializer = UserRegistrationSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogoutView(APIView):
    @staticmethod
    def post(request):
        logout(request)
        return Response({'message': 'Successfully Logged out'}, status=status.HTTP_200_OK)


class UserUpdateView(APIView):
    permission_classes = [IsAuthenticated, ]

    @staticmethod
    def update(request, pk, *args, **kwargs):
        user_obj = RestaurantUser.objects.get(pk)
        serializer = UserUpdateSerializers(user_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserChangePasswordView(APIView):
    permission_classes = [IsAuthenticated, ]

    @staticmethod
    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'old-password': openapi.Schema(type=openapi.TYPE_STRING, title='Current Password', example='123@abc'),
            'new-password': openapi.Schema(type=openapi.TYPE_STRING, title='New Password', example='123@efg'),
        }
    ))
    def post(request, *args, **kwargs):
        serializer = UserPasswordChangeSerializers(context={'request': request}, data=request.data)
        if serializer.is_valid():
            request.user.set_password(serializer.validated_data['new_password']).save()
            return Response({'message': 'Success'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




