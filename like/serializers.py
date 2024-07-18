from rest_framework import serializers,status
from rest_framework.exceptions import APIException

from .models import Like

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['LID', 'like_date', 'PID', 'UID']

        def create(self, validated_data):
            like = Like.objects.create(**validated_data)
            return like
        