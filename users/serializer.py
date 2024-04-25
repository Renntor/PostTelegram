from rest_framework.serializers import ModelSerializer
from .models import User


class UserSerializers(ModelSerializer):

    class Meta:
        model = User
        fields = ('telegram_id', 'telegram_name',)
        extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data: dict):
            password = validated_data.pop('password')
            user = User(**validated_data)
            user.set_password(password)
            user.save()
            return user
