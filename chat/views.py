from rest_framework import generics, permissions
from .models import Conversation, Message
from .serializers import ConversationDetailSerializer, MessageSerializer, ConversationSerializer

class ConversationListCreateView(generics.ListCreateAPIView):
    serializer_class = ConversationSerializer
    permission_class = [permissions.IsAuthenticated]
    # permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Conversation.objects.filter(user=self.request.user)  # user can only see their own conversations
        # return Conversation.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # new conversation automatically assign to logged in user
        # serializer.save() # TEMPORARY

class ConversationDetailView(generics.RetrieveAPIView):
    serializer_class = ConversationDetailSerializer
    permission_class = [permissions.IsAuthenticated]
    # permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Conversation.objects.filter(user=self.request.user)
        # return Conversation.objects.all()