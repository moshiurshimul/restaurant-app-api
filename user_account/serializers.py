from rest_framework import serializers

from user_account.models import RestaurantUser


class UserRegistrationSerializers(serializers.ModelSerializer):

    class Meta:
        model = RestaurantUser
        fields = ('username', 'password', 'email', 'phone_number', )


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
