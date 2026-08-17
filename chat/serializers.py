from rest_framework import serializers
from .models import Conversation, Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ["id", "role", "content", "tool_name", "tool_args", "status", "created_at"]
        read_only_fields = fields
    
class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = ["id", "title", "user", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]

class ConversationDetailSerializer(serializers.ModelSerializer):
    """
    Message is a nested serializer inside ConversationDetailSerializer. When you retrieve a single conversation, all the messages belonging to that conversation are included inside it because we have set related_name in the Message model. (related_name="messages")
    """
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Conversation
        fields = ["id", "title", "created_at", "updated_at", "messages"]