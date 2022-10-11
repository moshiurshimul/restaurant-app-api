from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from user_account.models import RestaurantUser


class UserRegistrationSerializers(serializers.ModelSerializer):

    class Meta:
        model = RestaurantUser
        fields = ('username', 'password', 'email', 'phone_number', )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = RestaurantUser.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            password=make_password(validated_data['password']),
            phone_number=validated_data['phone_number'],
        )
        user.save()
        return user


class UserUpdateSerializers(serializers.ModelSerializer):

    class Meta:
        model = RestaurantUser
        fields = ('first_name', 'last_name', 'email', 'phone_number', )


class UserPasswordChangeSerializers(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_current_password(self, value):
        if not self.context['request'].user.check_password(value):
            raise serializers.ValidationError({'current_password': 'Does not match'})
        return value
