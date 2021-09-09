from rest_framework import serializers
from ..models import *


class MessageSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    text = serializers.CharField(required=True)

    class Meta:
        model = Message
        fields = ["id", "email", "text"]
