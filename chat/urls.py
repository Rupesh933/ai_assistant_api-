from django.urls import path
from .views import ConversationListCreateView, ConversationDetailView


urlpatterns = [


    path("conversations/", ConversationListCreateView.as_view(), name="conversation-list"),
    path("conversations/<uuid:pk>/", ConversationDetailView.as_view(), name="conversation-detail")
]