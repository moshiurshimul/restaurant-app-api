from django.contrib.auth import logout
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from user_account.models import RestaurantUser
from user_account.serializers import UserRegistrationSerializers, UserUpdateSerializers, UserPasswordChangeSerializers


class UserRegistrationView(APIView):
    @staticmethod
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
    def post(request, *args, **kwargs):
        serializer = UserPasswordChangeSerializers(context={'request': request}, data=request.data)
        if serializer.is_valid():
            request.user.set_password(serializer.validated_data['new_password']).save()
            return Response({'message': 'Success'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




